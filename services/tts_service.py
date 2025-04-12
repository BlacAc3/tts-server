from services.groq_client import get_groq_client

def generate_speech(text, voice, output_file_path):
    """
    Generate speech from text using Groq API

    Args:
        text: Text to convert to speech
        voice: Voice to use
        output_file_path: Path to save the audio file

    Returns:
        Path to the generated audio file
    """
    client = get_groq_client()

    response = client.audio.speech.create(
        model="playai-tts",
        voice=voice,
        response_format="wav",
        input=text,
    )

    response.stream_to_file(output_file_path)

    return output_file_path
