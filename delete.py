import os
import shutil
from flask import redirect, abort
from auth import login_required

BASE_DIR = os.path.abspath("shared")

@login_required
def delete(path):
    """
    Delete a file or folder safely
    """

    # Convert URL path → real path
    target_path = os.path.join(BASE_DIR, path)

    # SECURITY CHECK
    if not os.path.commonpath([BASE_DIR, target_path]) == BASE_DIR:
        abort(403)

    # Must exist
    if not os.path.exists(target_path):
        abort(404)

    # If it is a FILE
    if os.path.isfile(target_path):
        os.remove(target_path)

    # If it is a FOLDER
    elif os.path.isdir(target_path):
        shutil.rmtree(target_path)

    # Redirect to parent folder
    parent = os.path.dirname(path)

    if parent:
        return redirect(f"/browse/{parent}")
    else:
        return redirect("/")
