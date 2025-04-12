from groq import Groq
from config import Config

def get_groq_client():
    """Return a configured Groq client"""
    client = Groq(api_key=Config.GROQ_API_KEY)
    return client
