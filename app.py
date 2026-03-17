from flask import Flask
from auth import login, logout
from upload import upload
from files import browse
from folders import create_folder
from delete import delete
from rename import rename
from zip_download import download_zip
from zip_upload import upload_zip

app = Flask(__name__)
app.secret_key = "super-secret-key"  # REQUIRED for flash


# added and updated routes
app.add_url_rule("/", "root", browse)
app.add_url_rule("/browse/<path:path>", "browse", browse)

app.add_url_rule("/login", "login", login, methods=["GET", "POST"])
app.add_url_rule("/logout", "logout", logout)

# upload routes
app.add_url_rule("/upload", "upload_root", upload, methods=["GET", "POST"])
app.add_url_rule("/upload/<path:path>", "upload", upload, methods=["GET", "POST"])

# folder creation routes
app.add_url_rule(
    "/create-folder",
    "create_folder_root",
    create_folder,
    methods=["GET", "POST"]
)

app.add_url_rule(
    "/create-folder/<path:path>",
    "create_folder",
    create_folder,
    methods=["GET", "POST"]
)

# rename file and folder route
app.add_url_rule(
    "/rename/<path:path>",
    "rename",
    rename,
    methods=["GET", "POST"]
)

# delete folder and files route
app.add_url_rule(
    "/delete/<path:path>",
    "delete",
    delete
)

# zip download folder
app.add_url_rule(
    "/download-zip/<path:path>",
    "download_zip",
    download_zip
)

# upload and extract zip file
app.add_url_rule(
    "/upload-zip",
    "upload_zip_root",
    upload_zip,
    methods=["POST"]
)
app.add_url_rule(
    "/upload-zip/<path:path>",
    "upload_zip",
    upload_zip,
    methods=["POST"]
)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
