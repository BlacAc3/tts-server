import os
import tempfile

class Config:
    # Base directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()

    # Server settings
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))

    # # Folder settings
    # UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    # OUTPUT_FOLDER = os.path.join(BASE_DIR, 'output')

    # Use /tmp directory for Vercel (or configured directory for local development)
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', os.path.join(tempfile.gettempdir(), 'uploads'))
    OUTPUT_FOLDER = os.getenv('OUTPUT_FOLDER', os.path.join(tempfile.gettempdir(), 'output'))

    # API settings
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')

    # File settings
    ALLOWED_AUDIO_EXTENSIONS = {'oga', 'ogg', 'mp3', 'wav'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload size
