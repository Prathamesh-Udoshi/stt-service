import os
import shutil
import uuid
import logging
from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from app.services.stt_service import stt_service
from app.core.config import settings

router = APIRouter()
logger = logging.getLogger(__name__)

# List of allowed audio extensions
ALLOWED_EXTENSIONS = {".mp3", ".wav", ".m4a", ".ogg", ".flac"}
MAX_FILE_SIZE = 25 * 1024 * 1024  # 25MB

def cleanup_file(path: str):
    """Deletes temporary files after processing."""
    try:
        if os.path.exists(path):
            os.remove(path)
            logger.info(f"Temporary file {path} deleted.")
    except Exception as e:
        logger.error(f"Failed to delete temp file {path}: {str(e)}")

@router.post("/transcribe/")
async def transcribe_audio(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):
    # 1. Validate file extension
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400, 
            detail=f"Unsupported file format. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"
        )

    # 2. Store file temporarily
    temp_filename = f"{uuid.uuid4()}{file_ext}"
    temp_path = os.path.join(settings.TEMP_DIR, temp_filename)

    try:
        with open(temp_path, "wb") as buffer:
            # Read in chunks to handle memory efficiently
            content = await file.read()
            if len(content) > MAX_FILE_SIZE:
                raise HTTPException(status_code=413, detail="File too large (Max 25MB)")
            buffer.write(content)
        
        # 3. Perform transcription
        transcription_text = stt_service.transcribe(temp_path)
        
        # 4. Schedule cleanup in background
        background_tasks.add_task(cleanup_file, temp_path)
        
        return {
            "filename": file.filename,
            "transcription": transcription_text,
            "status": "success"
        }

    except HTTPException as he:
        # Re-raise HTTP exceptions
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise he
    except Exception as e:
        # Log and handle general exceptions
        logger.error(f"Transcription endpoint error: {str(e)}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise HTTPException(status_code=500, detail="Internal server error during transcription.")
