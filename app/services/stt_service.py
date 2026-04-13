import logging
from faster_whisper import WhisperModel
from app.core.config import settings
import torch

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class STTService:
    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(STTService, cls).__new__(cls)
            cls._instance._load_model()
        return cls._instance

    def _load_model(self):
        """Loads the Faster-Whisper model according to configuration."""
        try:
            device = settings.DEVICE
            compute_type = settings.COMPUTE_TYPE
            
            # Auto-detect CUDA if device is 'cpu' but GPU is available
            if device == "cpu" and torch.cuda.is_available():
                logger.info("GPU detected! Defaulting to CUDA for faster inference.")
                device = "cuda"
                compute_type = "float16" # Recommended for GPU
            
            logger.info(f"Loading Whisper model '{settings.MODEL_NAME}' on {device} with {compute_type}...")
            
            self._model = WhisperModel(
                settings.MODEL_NAME, 
                device=device, 
                compute_type=compute_type
            )
            logger.info("Model loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load Whisper model: {str(e)}")
            raise e

    def transcribe(self, audio_path: str) -> str:
        """Transcribes the given audio file and returns the concatenated text."""
        try:
            segments, info = self._model.transcribe(audio_path, beam_size=5)
            
            logger.info(f"Detected language '{info.language}' with probability {info.language_probability:.2f}")
            
            # Concatenate segment text
            full_text = " ".join([segment.text.strip() for segment in segments])
            return full_text
        except Exception as e:
            logger.error(f"Transcription error: {str(e)}")
            raise e

# Create a singleton instance
stt_service = STTService()
