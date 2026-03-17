import os
from auth import login_required 
from flask import send_from_directory # Sends a file to browser for download
from flask import render_template # Sends data to HTML page
## abort added for navigatioon to folder subfoler
from flask import abort # for stopping request and show error page
from datetime import datetime  # for showing human readable date
from flask import request # for implementing sorting feature

# SHARED_DIR = "shared"

# BASE_DIR = os.path.abspath("shared")  #C:/intel/imp/flask_file_server/shared

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "shared")
)


@login_required # Before entering this function, check login
def browse(path=""):  # path comes from the URL
    """
    This function:
    - Lists folders and files
    - Allows navigation into subfolders
    """

    # Read sorting parameters from URL
    sort_by = request.args.get("sort", "name")   # default sorting by name
    order = request.args.get("order", "asc")     # default ascending order
    
    # Read search query from URL
    search = request.args.get("search", "").lower()

    # File type filter from URL
    file_type = request.args.get("type", "all")


    # Convert URL path to real folder path
    full_path = os.path.join(BASE_DIR, path)
    # path = "remote/school"
    # full_path = "shared/remote/sub folder"


    # Security check
    if not os.path.commonpath([BASE_DIR, full_path]) == BASE_DIR:
        # commonpath(): It finds the common part of two paths.
        # BASE_DIR = shared
        # full_path = shared/remote
        # Common path = shared
        abort(403) 

        # Common path ≠ shared
        # abort(403) → Access denied


    # If path does not exist
    if not os.path.exists(full_path):
        abort(404) 

    # If path is a file → download it
    if os.path.isfile(full_path):
        # path = "remote/sub folder/demo.txt"

        folder = os.path.dirname(path)  # remote/sub folder
        filename = os.path.basename(path) # demo.txt
        return send_from_directory(
            os.path.join(BASE_DIR, folder), # shared/remote/sub folder
            filename,
            as_attachment=True # Browser downloads file
        )

    # If path is a folder → list contents
    items = []
    total_size = 0   # <-- ADD THIS

    for name in os.listdir(full_path): # shared/remote
        item_path = os.path.join(full_path, name) # shared/remote/web.html
        is_dir = os.path.isdir(item_path)

        # determine File size
        if is_dir:
            size = "-"
        else:
            size = os.path.getsize(item_path) #Returns size in bytes
            total_size += size   # <-- ADD THIS

        
        # Last modified time of file
        modified_ts = os.path.getmtime(item_path) #1706624123.0   ← timestamp
        modified = datetime.fromtimestamp(modified_ts).strftime("%Y-%m-%d %H:%M") #2026-01-30 14:22

        ext = ""
        if not is_dir and "." in name:
            ext = name.rsplit(".", 1)[1].lower()


        items.append({
            "name": name,
            "is_dir": is_dir,
            "size": size,
            "modified": modified,
            "ext": ext

        })

    
    # ---------------- Build breadcrumb navigation -----------------

    breadcrumbs = []

    # Root breadcrumb
    breadcrumbs.append({
        "name": "Home",
        "path": ""
    })

    # If user is inside folders
    if path:
        parts = path.split("/")   # ['remote','school','notes']

        current = ""

        for part in parts:
            if current:
                current = current + "/" + part
            else:
                current = part

            breadcrumbs.append({
                "name": part,
                "path": current
            })

    # ---------------- End of Build breadcrumb navigation -----------------
    # print(breadcrumbs)

   # ----------------------- Search Filtering ---------------------

    if search:
        filtered = []

        for item in items:
            if search in item["name"].lower():
                filtered.append(item)

        items = filtered

   # ----------------------- End of Search Filtering ---------------------


    # ----------------------- File Type Filtering ---------------------

    if file_type != "all":

        type_map = {
            "image": ["png","jpg","jpeg","gif","svg","webp"],
            "document": ["pdf","doc","docx","txt","md"],
            "spreadsheet": ["xls","xlsx","csv"],
            "archive": ["zip","rar","7z","tar","gz"],
            "code": ["py","js","html","css","json","java","c","cpp"],
            "media": ["mp4","mkv","mov","avi","mp3","wav","ogg"]
        }

        allowed_ext = type_map.get(file_type, [])

        items = [
            item for item in items
            if item["ext"] in allowed_ext
        ]
    # -----------------------End of File Type Filtering ---------------------

    # ------------------------ Sorting Logic --------------------------

    reverse = True if order == "desc" else False
    # reverse=True means descending order

    if sort_by == "name":
        items.sort(key=lambda x: x["name"].lower(), reverse=reverse)

    elif sort_by == "size":
        # folders have size "-" so treat them as 0
        items.sort(
            key=lambda x: x["size"] if isinstance(x["size"], int) else 0,
            reverse=reverse
        )

    elif sort_by == "modified":
        items.sort(key=lambda x: x["modified"], reverse=reverse)

    # SECOND SORT: keep folders on top
    items.sort(key=lambda x: not x["is_dir"])

    # -------------------------End of Sorting Logic ---------------------------


    return render_template(
        "browse.html",
        items=items,
        current_path=path,
        total_size=total_size,
        item_count=len(items),
        breadcrumbs=breadcrumbs,
        sort_by=sort_by,
        order=order,
        search=search,
        file_type=file_type
    )

# What items now looks like
# [
#   {
#     "name": "docs",
#     "is_dir": True,
#     "size": "-",
#     "modified": "2026-01-30 13:20"
#   },
#   {
#     "name": "notes.txt",
#     "is_dir": False,
#     "size": 2048,
#     "modified": "2026-01-30 14:01"
#   }
# ]
