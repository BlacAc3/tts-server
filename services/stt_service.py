from services.groq_client import get_groq_client
import os

def transcribe_audio(file_path, original_filename):
    """
    Transcribe audio file to text using Groq API

    Args:
        file_path: Path to the temporary audio file
        original_filename: Original filename (for content type)

    Returns:
        Transcription object from Groq
    """
    client = get_groq_client()

    try:
        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=(original_filename, audio_file.read()),
                model="whisper-large-v3",
                response_format="verbose_json",
            )

        return transcription
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        raise

    finally:
        # Clean up the temporary file
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            # Just log without raising since this is cleanup
            print(f"Error removing temporary file: {str(e)}")
