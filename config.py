import os
import tempfile

class Config:
    # Base directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Server settings
    DEBUG = os.environ.get('DEBUG', 'True') == 'True'
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5000))

    # # Folder settings
    # UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    # OUTPUT_FOLDER = os.path.join(BASE_DIR, 'output')

    # Use /tmp directory for Vercel (or configured directory for local development)
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', os.path.join(tempfile.gettempdir(), 'uploads'))
    OUTPUT_FOLDER = os.environ.get('OUTPUT_FOLDER', os.path.join(tempfile.gettempdir(), 'output'))

    # API settings
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY')

    # File settings
    ALLOWED_AUDIO_EXTENSIONS = {'oga', 'ogg', 'mp3', 'wav'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload size
