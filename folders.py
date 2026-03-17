# this module is for creating folder

import os
from flask import request, redirect, render_template, abort, url_for
from auth import login_required

BASE_DIR = os.path.abspath("shared")

@login_required
def create_folder(path=""):
    """
    Create a new folder inside the CURRENT folder
    """

    # Convert URL path → real folder path
    parent_dir = os.path.join(BASE_DIR, path)

    # SECURITY CHECK
    if not os.path.commonpath([BASE_DIR, parent_dir]) == BASE_DIR:
        abort(403)

    # Parent folder must exist
    if not os.path.exists(parent_dir):
        abort(404)

    # Show form
    if request.method == "GET":
        return render_template(
            "create_folder.html",
            current_path=path
        )

    # Handle form submit
    folder_name = request.form.get("folder_name", "").strip()

    if not folder_name:
        return render_template("create_folder.html", error="Folder name required")
        # return "Folder name required", 400

    # Prevent path tricks like ../
    if "/" in folder_name or "\\" in folder_name:
        return render_template("create_folder.html", error="Invalid folder name")
        # return "Invalid folder name", 400

    # Full path of new folder
    new_folder_path = os.path.join(parent_dir, folder_name)

    if os.path.exists(new_folder_path):
        return render_template("create_folder.html", error="Folder already exists")
        # return "Folder already exists", 400

    os.mkdir(new_folder_path)

    # Redirect back to current folder
    if path:
        return redirect(f"/browse/{path}")
    else:
        return redirect("/")
