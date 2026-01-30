# 📝 Notes App API (FastAPI)

A simple backend API for managing notes, built with **FastAPI**, featuring **JWT authentication (Access & Refresh Tokens)**. This project is suitable for learning purposes or as a starter backend for larger applications.

---

## 🚀 Features

* 🔐 Authentication using:

  * Access Token (short-lived)
  * Refresh Token (automatic renewal)
* 🍪 Tokens stored in **HTTP-only Cookies**
* 🧠 Single dependency to protect all secured endpoints
* 🗒️ Full CRUD operations for notes
* ⚡ FastAPI with SQLAlchemy ORM
* 🧪 Optimized for local development

---

## 🛠️ Tech Stack

* **Python 3.11**
* **FastAPI**
* **SQLAlchemy**
* **Passlib (bcrypt)**
* **python-jose (JWT)**
* **SQLite** (default database)


---

## 📂 Project Structure

```
Notes-App-Api/
│
├── alembic/                # Database migrations
├── alembic.ini             # Alembic configuration
│
├── api/
│   └── v1/
│       └── routes/         # API v1 routes
│
├── auth/                   # Authentication & JWT logic
├── core/                   # Core settings & security utilities
├── database_settings/      # Database configuration & session
├── schemas/                # Pydantic schemas
├── services/               # Business logic layer
├── tests/                  # Tests
│
├── main.py                 # Application entry point
├── requirements.txt        # Project dependencies
└── README.md
```

---

## 🔐 Authentication Flow

1. User logs in
2. Server returns:

   * Access Token (stored in a cookie)
   * Refresh Token (stored in a cookie)
3. For any protected endpoint:

   * If the access token is valid → request is allowed
   * If the access token is expired or about to expire → refresh token is used automatically
   * If both tokens are invalid → Unauthorized response

---

## ⚙️ Installation & Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/USERNAME/Notes-App-Api.git
cd Notes-App-Api
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\\Scripts\\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the server

```bash
uvicorn app.main:app --reload
```

📍 API will be available at:

```
http://127.0.0.1:8000
```

📘 Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## 🍪 Cookie Settings (Local Development)

```python
secure=False
httponly=True
samesite="lax"
```

> ⚠️ In production, make sure to set `secure=True` and use HTTPS.

---

## 📌 Environment Variables (.env)

````env
# Database (SQLite)
DATABASE_URL=sqlite:///./data.db

# JWT Settings
ACCESS_TOKEN_SECRET_KEY=your_access_secret
REFRESH_TOKEN_SECRET_KEY=your_refresh_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
```env
ACCESS_TOKEN_SECRET_KEY=your_access_secret
REFRESH_TOKEN_SECRET_KEY=your_refresh_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
````

---

## 🧪 Testing

You can test the API using:

* Swagger UI (`/docs`)
* Postman or Insomnia

Make sure cookies are enabled when testing authentication.

---

## 📄 License

This project is open-source and available for learning and personal use.

---

## 👤 Author

**Zeyad Ossama**

Feel free to fork the project, open issues, or suggest improvements 🚀
