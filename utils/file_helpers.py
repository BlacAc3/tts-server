import os
from werkzeug.utils import secure_filename

def allowed_file(filename, allowed_extensions):
    """Check if file has an allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def save_temp_file(file_obj, upload_folder):
    """
    Save uploaded file to a temporary location

    Args:
        file_obj: Flask file object
        upload_folder: Folder to save the file

    Returns:
        Path to the saved file
    """
    filename = secure_filename(file_obj.filename)
    filepath = os.path.join(upload_folder, filename)
    file_obj.save(filepath)
    return filepath
