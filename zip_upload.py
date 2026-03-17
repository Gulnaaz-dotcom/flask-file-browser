import os
import zipfile
from flask import request, redirect, abort
from werkzeug.utils import secure_filename
from auth import login_required

BASE_DIR = os.path.abspath("shared")  #C:/intel/imp/flask_file_server/shared

@login_required
def upload_zip(path=""):

    """
    upload and extract a ZIP of a folder onto server
    """
     
    target_dir = os.path.join(BASE_DIR, path) #C:\Intel\imp\flask_file_server\shared\remote/info

    # Security check
    if not os.path.commonpath([BASE_DIR, target_dir]) == BASE_DIR:
        abort(403)

    if not os.path.exists(target_dir):
        abort(404)

    zip_file = request.files.get("zipfile")

    if not zip_file or not zip_file.filename.endswith(".zip"):
        return "Invalid ZIP file", 400

    # Safe ZIP filename
    zip_name = secure_filename(zip_file.filename)
    zip_path = os.path.join(target_dir, zip_name)

    # Save ZIP temporarily
    zip_file.save(zip_path)

    # Extract ZIP
    with zipfile.ZipFile(zip_path, "r") as zipf:
        for member in zipf.namelist():

            # Prevent zip-slip attack
            extracted_path = os.path.normpath(
                os.path.join(target_dir, member)
            )

            if not os.path.commonpath([BASE_DIR, extracted_path]) == BASE_DIR:
                continue  # skip unsafe file

            zipf.extract(member, target_dir)

    # Remove ZIP after extraction
    os.remove(zip_path)

    return redirect(f"/browse/{path}" if path else "/")
