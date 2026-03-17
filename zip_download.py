import os
import zipfile
from io import BytesIO
from flask import send_file, abort
from auth import login_required

BASE_DIR = os.path.abspath("shared") #C:/intel/imp/flask_file_server/shared

@login_required
def download_zip(path):

    # path comes from URL
    # /download-zip/remote/school
    # path = "remote/school"

    """
    Create and download a ZIP of a folder
    """

    # Convert URL path → real folder path
    folder_path = os.path.join(BASE_DIR, path) #C:\Intel\imp\flask_file_server\shared\remote/info

    # Security check
    if not os.path.commonpath([BASE_DIR, folder_path]) == BASE_DIR:
        abort(403)

    # Must exist and be folder
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        abort(404)

    # Create ZIP buffer in memory
    zip_buffer = BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                full_file_path = os.path.join(root, file)

                # Path inside zip (relative)
                arcname = os.path.relpath(full_file_path, folder_path)

                # Add file to ZIP
                zipf.write(full_file_path, arcname)

    zip_buffer.seek(0)

    zip_name = os.path.basename(path) + ".zip"
    
    # # the URL is : 192.168.0.150:8000/browse/remote
    # print("Path:", path) #remote/info
    # print("Folder path:", folder_path) # C:\Intel\imp\flask_file_server\shared\remote/info
    # print("Adding file:", full_file_path)
    # # C:\Intel\imp\flask_file_server\shared\remote/info\myLovelyNotes\python\web-db\__pycache__\db.cpython-312.pyc
    # print("ZIP path:", arcname) #myLovelyNotes\python\web-db\__pycache__\db.cpython-312.pyc

    return send_file(
        zip_buffer,
        mimetype="application/zip",
        as_attachment=True,
        download_name=zip_name
    )
