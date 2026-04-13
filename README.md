# Speech-to-Text Microservice (Soniq)

A dedicated, high-performance Speech-to-Text (STT) microservice built with **FastAPI** and **Faster-Whisper**. It features a modern web dashboard for easy transcription via audio uploads or live microphone recording.

## 🚀 Key Features
- **Modern Dashboard**: Clean, full-width web interface for managing transcriptions.
- **Live Recording**: Capture and transcribe audio directly from your microphone.
- **Fast Inference**: Powered by `faster-whisper` for optimized processing.
- **Auto Hardware Detection**: Automatically detects and utilizes GPU (CUDA) for lightning-fast results.
- **Smart Resource Cleanup**: Automatically deletes temporary audio files after processing.
- **API Ready**: Exposes a POST endpoint for integration with other services (e.g., Laravel).

## 🛠 Tech Stack
- **FastAPI**: Backend web framework.
- **Faster-Whisper**: Optimized re-implementation of OpenAI's Whisper model.
- **Vanilla JS/CSS**: Minimalist, high-performance frontend dashboard.
- **Pydantic Settings**: Centralized configuration management.

## 📂 Project Structure
- `app/main.py`: Application entry point and static file serving.
- `app/services/stt_service.py`: Singleton model loader and transcription logic.
- `app/api/routes.py`: Transcription API endpoints.
- `static/index.html`: Modern dashboard frontend.
- `temp/`: Internal temporary storage for audio processing.

## ⚙️ Setup & Installation

1. **Clone the repository**:
   ```powershell
   git clone https://github.com/Prathamesh-Udoshi/stt-service.git
   cd stt-service
   ```

2. **Create a Virtual Environment**:
   ```powershell
   python -m venv stt-env
   .\stt-env\Scripts\Activate.ps1
   ```

3. **Install Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the Service**:
   ```powershell
   python -m app.main
   ```

## 🖥 Usage

### Web Dashboard
Open your browser to: **`http://localhost:8001`**
- Click **"Upload Audio File"** to transcribe existing files.
- Click **"Record Live Mic"** to transcribe your voice in real-time.

### API Integration
**Endpoint**: `POST /api/v1/transcribe/`  
**Sample Curl Command**:
```powershell
curl -X POST "http://localhost:8001/api/v1/transcribe/" `
     -H "Content-Type: multipart/form-data" `
     -F "file=@audio.mp3"
```

## 📜 License
MIT
