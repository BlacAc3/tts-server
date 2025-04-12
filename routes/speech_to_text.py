from flask import Blueprint, request, jsonify
from services.stt_service import transcribe_audio
from utils.file_helpers import save_temp_file, allowed_file
from config import Config

stt_bp = Blueprint('speech_to_text', __name__)

@stt_bp.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    """
    Convert speech to text using Groq's STT API
    Accepts audio files in oga, ogg, mp3, wav formats
    """
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and allowed_file(file.filename, Config.ALLOWED_AUDIO_EXTENSIONS):
        return process_audio_file(file)

    return jsonify({"error": f"File not allowed. Supported formats: {', '.join(Config.ALLOWED_AUDIO_EXTENSIONS)}"}), 400

@stt_bp.route('/wav-to-text', methods=['POST'])
def wav_to_text():
    """
    Convert WAV audio to text using Groq's STT API
    Specifically for WAV format
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file and file.filename.lower().endswith('.wav'):
        return process_audio_file(file)

    return jsonify({"error": "File must be in WAV format"}), 400

def process_audio_file(file):
    """Process the uploaded audio file and return transcription"""
    try:
        temp_filepath = save_temp_file(file, Config.UPLOAD_FOLDER)
        transcription = transcribe_audio(temp_filepath, file.filename)

        # Return the transcription
        return jsonify({
            "text": transcription.text,
            "full_response": transcription
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
