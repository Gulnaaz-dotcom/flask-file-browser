# It handles file upload in shared folder with security and 
# authenticity check, also listling the newly uploaded file on browser
# also handles uploading folder or multiple files

import os
from flask import request, redirect, render_template, abort
from auth import login_required
from werkzeug.utils import secure_filename #for uploading folders
from flask import flash
from flask import get_flashed_messages

BASE_DIR = os.path.abspath("shared")

@login_required
def get_unique_path(path):
    """
    If file exists, auto-generate a new filename:
    example.txt -> example (1).txt -> example (2).txt
    """
    #path = "shared/Project/backup.bat"

    # Split full path into:
    # base path + extension
    base, ext = os.path.splitext(path)
    # base = "shared/Project/backup"
    # ext  = ".bat"

    counter = 1

    # Keep increasing counter until filename is unique
    while os.path.exists(path):
        path = f"{base} ({counter}){ext}"
        counter += 1

    return path


@login_required
def upload(path=""):
    """
    Upload a file into the CURRENT folder
    """

    # Convert URL path → real folder path
    upload_dir = os.path.join(BASE_DIR, path)

    # SECURITY CHECK (same idea as browse)
    if not os.path.commonpath([BASE_DIR, upload_dir]) == BASE_DIR:
        abort(403)

    # Folder must exist
    if not os.path.exists(upload_dir):
        abort(404)

    # If user opens upload page
    if request.method == "GET":
        return render_template(
            "upload.html",
            current_path=path
        )
    
    #### handling if folder uploads or input contain multiple files  ####

    # If user submits file
    # file = request.files.get("file")
    files = request.files.getlist("files")

    for file in files:
        if not file.filename:
            continue

        # IMPORTANT PART 👇
        # file.filename may contain folder structure
        # Example: "myfolder/sub/a.txt"
        
        if not file or file.filename == "":
            return "No file selected", 400

        relative_path = file.filename
        # secure_path = secure_filename(relative_path) // not needed

        # Split folders & filename
        full_path = os.path.join(upload_dir, relative_path)
        full_path = os.path.normpath(full_path)

        # Security re-check
        if not os.path.commonpath([BASE_DIR, full_path]) == BASE_DIR:
            continue

        # Create folders if needed
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        # If file already exists → collect conflict, and send the message
        # if os.path.exists(full_path):
        #     flash(f"File already exists: {os.path.basename(full_path)}", "error")
        #     print("CHECKING:", full_path) #C:\Intel\imp\flask_file_server\shared\Project\backup.bat
        #     print("EXISTS:", os.path.exists(full_path)) # return true or false
        #     print("FLASHES:", get_flashed_messages(with_categories=True))
        #     # FLASHES: [('error', 'File already exists: backup.bat')]
        #     continue

        # Auto-rename if file already exists
        full_path = get_unique_path(full_path)
        #print("CHECKING:", full_path) #C:\Intel\imp\flask_file_server\shared\Project\backup.bat

        # Save file
        file.save(full_path)

    print("UPLOAD PATH:", path) # Project
    print("FILES:", request.files) #ImmutableMultiDict([('files', <FileStorage: 'backup.bat' ('application/octet-stream')>)])

        
    # Go back to the folder where file was uploaded
    return redirect(f"/browse/{path}" if path else "/")


# f -> “Format this string by evaluating expressions inside it.”




    
