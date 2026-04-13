import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Speech-to-Text Microservice"
    PORT: int = 8001
    
    # Model Configuration
    # Options: "tiny", "base", "small", "medium", "large-v3"
    MODEL_NAME: str = "base"
    
    # Device Configuration: "cpu", "cuda"
    DEVICE: str = "cpu"
    
    # Compute Type: "int8", "float16", "float32"
    # "int8" is best for CPU, "float16" for GPU
    COMPUTE_TYPE: str = "int8"
    
    # Directory for temporary file storage
    TEMP_DIR: str = os.path.join(os.getcwd(), "temp")

    class Config:
        env_file = ".env"

settings = Settings()

# Ensure temp directory exists
os.makedirs(settings.TEMP_DIR, exist_ok=True)
