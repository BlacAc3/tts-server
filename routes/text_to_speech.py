from flask import Blueprint, request, jsonify, send_file
from services.tts_service import generate_speech
from werkzeug.utils import secure_filename
import os
import time
from config import Config

tts_bp = Blueprint('text_to_speech', __name__)

@tts_bp.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    """
    Convert text to speech using Groq's TTS API
    Expected JSON format: {"text": "Text to convert to speech", "voice": "Aaliyah-PlayAI"}
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    text = data.get('text')
    voice = data.get('voice', 'Aaliyah-PlayAI')  # Default voice

    if not text:
        return jsonify({"error": "No text provided"}), 400

    try:
        # Generate unique filename
        output_file = os.path.join(
            Config.OUTPUT_FOLDER,
            f"speech_{secure_filename(text[:20])}_{int(time.time())}.wav"
        )

        # Generate speech using service
        generate_speech(text, voice, output_file)

        return send_file(output_file, as_attachment=True, download_name="speech.wav")

    except Exception as e:
        return jsonify({"error": str(e)}), 500
