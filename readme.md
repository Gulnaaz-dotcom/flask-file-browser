# 🔐 Flask File Browser (Secure Web-Based File Manager)

A full-featured **web-based file management system** built using Flask that allows users to securely upload, organize, and manage files and folders through an intuitive browser interface.

This project demonstrates backend engineering, authentication systems, and practical file handling in a real-world application scenario.

---

## Key Features

* Upload files and entire folders
* ZIP upload and extract folders
* Drag-and-drop files and folder upload
* ZIP download folders
* Create, rename, and delete folders
* Rename, and delete files
* Breadcrumb navigation for seamless directory traversal
* User authentication (login/signup/logout)
* Search sort and filter functionality
* Secure file handling and access control
* Clean and structured UI for file management

---

## 🛠 Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** PostgreSQL 

---


## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Gulnaaz-dotcom/flask-file-browser.git

# Navigate into the project
cd flask-file-browser

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

---

## Authentication System

* Secure user registration and login
* Session-based authentication
* Protected routes to restrict unauthorized access
* Password handling using hashing (recommended: Werkzeug security)

---

## Project Structure

```
flask-file-browser/
│── app.py
│── auth.py
│── delete.py
│── files.py
│── folders.py
│── rename.py
│── upload.py
│── zip_download.py
│── zip_upload.py
│── templates/
│── static/
│── shared/
│── requirements.txt
│── readme.md
```

---

## What This Project Demonstrates

* Backend development with Flask
* Routing and request handling
* File system operations in Python
* Authentication and session management
* Clean project structuring and modular design

---

## 🚧 Future Improvements

* File preview (images, PDFs, etc.)
* Role-based access control (admin/user)
* Cloud storage integration (AWS S3 / Firebase)

---

## 🌐 Use Case

This project simulates a **mini cloud storage/file manager**, similar in concept to systems like Google Drive, focusing on core backend logic and secure file operations.

---

## 👨‍💻 Author

**Gulnaaz**

* GitHub: [https://github.com/Gulnaaz-dotcom](https://github.com/Gulnaaz-dotcom)
---

## Notes for Recruiters

This project was built to demonstrate:

* Strong understanding of backend development using Flask
* Ability to design and implement real-world features like authentication and file management
* Clean, maintainable, and scalable code practices



