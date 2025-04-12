from app import app

# This serves as an entry point for Vercel serverless functions
# The app is imported from app.py

# Export the Flask app for Vercel
handler = app
