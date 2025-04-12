from flask import Blueprint
from routes.speech_to_text import stt_bp
from routes.text_to_speech import tts_bp

def register_routes(app):
    """Register all route blueprints"""
    app.register_blueprint(stt_bp)
    app.register_blueprint(tts_bp)
