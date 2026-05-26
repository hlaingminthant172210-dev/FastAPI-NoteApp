# FastAPI Note App

A simple backend API built with FastAPI and MongoDB for managing notes with user authentication and password hashing.

---

## 🚀 Features

- User Registration
- User Login
- JWT Authentication
- Password Hashing using bcrypt
- Create Notes
- Get All Notes
- Get Note by ID
- Update Notes
- Delete Notes

---

## 🧱 Project Structure

```bash
Add
    CRUD/
        note.py
        user.py
    
    Models/
        note.py
        user.py
    
    Routes/
        config.py
        db.py
        main.py
        note.py
        user.py
    
    utils/
        authentication.py
        password.py
    
    .gitignore
    deletedata.py
```

---

## ⚙️ Tech Stack

- Python 3.13.12
- FastAPI
- MongoDB
- PyMongo / Motor
- JWT Authentication
- Passlib
- bcrypt 4.2.0 (for python 3.13)
- Pydantic

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/hlaingminthant172210-dev/FastAPI-NoteApp.git  

```

### 2. Move into project directory

```bash
cd fastAPI-NoteApp
```

### 3. Create virtual environment

```bash
python3 -m venv myenv
```

### 4. Activate virtual environment

Linux:

```bash
source myenv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the project

```bash
uvicorn App.Routes.main:app --reload
```

---

## 🔐 Authentication Flow

1. Register a new user
2. Password is hashed using bcrypt
3. Login with email and password
4. JWT token is generated
5. Use token to access protected routes

---

## 📌 API Endpoints

### 👤 User Routes

- POST `/register`
- POST `/login`

### 📝 Note Routes

- POST `/notes`
- GET `/notes`
- GET `/notes/{id}`
- PUT `/notes/{id}`
- DELETE `/notes/{id}`

---

## 🧠 Purpose

This project was built while learning:

- FastAPI backend development
- MongoDB integration
- CRUD operations
- JWT authentication
- Password hashing
- Backend project structure

---

## 👨‍💻 Author

Built as a backend learning project using FastAPI and MongoDB.
