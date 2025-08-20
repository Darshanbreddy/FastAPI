# 🛡️ Secure Blog API with FastAPI, PostgreSQL & JWT

A secure, high-performance RESTful API built using **FastAPI**, **PostgreSQL**, **JWT Authentication**, and **SQLAlchemy ORM**. This project supports full **CRUD operations** for blog posts and user management with password hashing and token-based login.

---

## 🚀 Features

- 🔐 JWT-based OAuth2 authentication
- 🔄 CRUD APIs for users and posts
- 🧾 SQLAlchemy ORM with PostgreSQL
- 🧪 Input validation with Pydantic
- 📂 Modular FastAPI structure with routers
- 📑 Auto-generated API docs with Swagger UI

---

## 🛠️ Tech Stack

- **FastAPI** – high-performance Python web framework
- **PostgreSQL** – relational database
- **SQLAlchemy** – ORM for database interactions
- **Pydantic** – schema validation
- **JWT / OAuth2** – secure authentication
- **bcrypt** – password hashing
---

## 📁 Project Structure

├── app
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
│ ├── utils.py
│ ├── oauth2.py
│ └── routes
│ ├── auth.py
│ ├── users.py
│ └── posts.py

---

## 🔐 Authentication Flow

1. User logs in via `/login` with email and password
2. JWT token is issued and must be included in all protected routes (`Authorization: Bearer <token>`)
3. Token is decoded to validate access to resources

---

## 🧪 API Endpoints (Examples)

| Method | Endpoint        | Description              |
|--------|------------------|--------------------------|
| POST   | `/login`         | Login and get JWT token  |
| POST   | `/users/`        | Register a new user      |
| GET    | `/users/{id}`    | Get user by ID           |
| GET    | `/posts/`        | Get all posts            |
| POST   | `/posts/`        | Create a new post        |
| PUT    | `/posts/{id}`    | Update an existing post  |
| DELETE | `/posts/{id}`    | Delete a post            |

---

## 🧰 Getting Started

### 🔧 Requirements
- Python 3.9+
- PostgreSQL

### 💻 Setup

```bash
# Clone repo
git clone https://github.com/Darshanbreddy/FastAPI.git
cd FastAPI

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
