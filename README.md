# Speech-to-Text Microservice

A dedicated microservice built with **FastAPI** and **Faster-Whisper** to handle high-performance audio transcription.

## Features
- **Fast Inference**: Uses `faster-whisper` for optimized transcription.
- **Auto GPU Detection**: Automatically uses CUDA if a compatible GPU is found.
- **Scalable Structure**: Modularized code for easy maintenance and scaling.
- **Resource Management**: Automatically cleans up temporary audio files after processing.
- **CORS Enabled**: Ready to be consumed by web applications (e.g., Laravel).

## Tech Stack
- **FastAPI**: Modern, fast web framework.
- **Faster-Whisper**: A re-implementation of OpenAI's Whisper model using CTranslate2.
- **Uvicorn**: Lightning-fast ASGI server.
- **Python-Multipart**: For handling audio file uploads.

## Setup & Installation

1. **Create a Virtual Environment**:
   ```powershell
   python -m venv stt-env
   .\stt-env\Scripts\Activate.ps1
   ```

2. **Install Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Configure Environment (Optional)**:
   Create a `.env` file in the root directory to override default settings:
   ```env
   MODEL_NAME=base
   PORT=8001
   DEVICE=cpu
   ```

## Running the Service

Start the server using the module command:
```powershell
python -m app.main
```

The service will be available at `http://localhost:8001`.

## Documentation
Once running, you can access the interactive Swagger UI at:
👉 **`http://localhost:8001/docs`**

## API Reference

### Transcribe Audio
**Endpoint**: `POST /api/v1/transcribe/`  
**Content-Type**: `multipart/form-data`

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `file` | File | Yes | Audio file (mp3, wav, m4a, etc.) |

**Sample Curl Command**:
```powershell
curl -X POST "http://localhost:8001/api/v1/transcribe/" `
     -H "accept: application/json" `
     -H "Content-Type: multipart/form-data" `
     -F "file=@path/to/audio.mp3"
```

**Response**:
```json
{
  "filename": "audio.mp3",
  "transcription": "The transcribed text goes here...",
  "status": "success"
}
```

## Future Enhancements
- [ ] Batch processing support.
- [ ] Async processing with Celery/Redis for long files.
- [ ] Support for custom vocabularies.
- [ ] Language detection only endpoint.
