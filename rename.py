# this file handles renaming file and folder
# also hanldes if user renamed nothing and submit
# and if the the new name given on form, with te same name other file and folder
# exist already in that directory

import os
from flask import request, render_template, redirect, abort
from auth import login_required
from flask import flash

BASE_DIR = os.path.abspath("shared")

@login_required
def rename(path):
    """
    Rename a file or folder safely
    """

    # Convert URL path → real filesystem path
    old_path = os.path.join(BASE_DIR, path)

    # Parent directory (used for redirect & new path)
    parent_dir = os.path.dirname(old_path)
    
    # Parent directory (used for redirect & new path)
    # parent = os.path.dirname(path)

    # Get the old name
    old_name = os.path.basename(old_path)

    # SECURITY CHECK
    if not os.path.commonpath([BASE_DIR, old_path]) == BASE_DIR:
        abort(403)

    # Must exist
    if not os.path.exists(old_path):
        abort(404)
       
    # Split old name into base + extension
    base_name, extension = os.path.splitext(old_name)
    
    # Show rename form
    if request.method == "GET":
        return render_template(
            "rename.html",
            current_path=path,
            display_name= base_name if os.path.isfile(old_path) else old_name,
            extension=extension if os.path.isfile(old_path) else "",
            is_file=os.path.isfile(old_path),
            current_name= base_name
        )

    ### Handle form submit
    new_name = request.form.get("new_name", "").strip()

    if not new_name:
        # return "New name required", 400  #shwoing the white bank page with message
        return redirect(request.referrer)
    
    # Prevent path tricks
    if "/" in new_name or "\\" in new_name:
        return "Invalid name", 400
    

    # If original item is a FILE → force same extension
    if os.path.isfile(old_path):
        new_name = new_name + extension
   
    # Build new path
    new_path = os.path.join(parent_dir, new_name)


    # CASE 1: Name unchanged → do nothing
    if new_name == old_name:
        return redirect(request.referrer)

    if os.path.exists(new_path):
        flash("A file or folder with this name already exists.", "error")
        return redirect(request.referrer)

 
    # Rename operation
    os.rename(old_path, new_path)
    return redirect(request.referrer)

    # # Redirect back to parent folder
    # if parent:
    #     return redirect(f"/browse/{parent}")
    # else:
    #     return redirect("/")
