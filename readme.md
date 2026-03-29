# 🔐 Flask File Browser (Secure Web-Based File Manager)

A **full-stack web-based file management system** built with Flask and PostgreSQL, designed to provide users with a secure and intuitive interface for managing files and directories online. 

The application emphasizes robust backend architecture, efficient file handling, and user-centric design, simulating real-world cloud storage functionality.

---

## Key Features

* Secure user authentication (signup, login, logout) with access control
* Upload files and entire folders, including ZIP upload with automatic extraction
* Download folders as ZIP archives
* Create, rename, and delete files and directories
* Drag-and-drop interface for seamless file uploads
* Breadcrumb navigation for intuitive directory traversal
* Advanced search, sorting, and filtering capabilities
* Structured and responsive UI built with Bootstrap
* Secure file storage and handling to prevent unauthorized access

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



