# 🚀 FastAPI Modular CRUD Application

A clean and scalable FastAPI project demonstrating CRUD operations using a modular architecture with SQLAlchemy and SQLite.

---

## 📌 Features

- Modular project structure  
- CRUD APIs (Create, Read, Update, Delete)  
- SQLAlchemy ORM integration  
- Pydantic validation  
- SQLite database  
- Easy to scale for production  

---

## 📁 Project Structure

fastapi_project/
│── main.py  
│── database.py  
│── models.py  
│── schemas.py  
│── crud.py  
│── routers/  
│     └── employee.py  

---

## 🧱 Tech Stack

- FastAPI  
- Python  
- SQLAlchemy  
- SQLite  
- Uvicorn  

---

## ⚙️ Setup Instructions

### 1. Clone Repository

git clone <your-repo-url>  
cd fastapi_project  

### 2. Create Virtual Environment

python -m venv venv  
source venv/bin/activate   # Linux/Mac  
venv\Scripts\activate      # Windows  

### 3. Install Dependencies

pip install fastapi uvicorn sqlalchemy  

---

## ▶️ Run Application

uvicorn main:app --reload  

App will run at:  
http://127.0.0.1:8000  

---

## 📖 API Documentation

Swagger UI:  
http://127.0.0.1:8000/docs  

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|---------|------------|
| POST   | /employees/       | Create employee |
| GET    | /employees/       | Get all employees |
| GET    | /employees/{id}  | Get single employee |
| PUT    | /employees/{id}  | Update employee |
| DELETE | /employees/{id}  | Delete employee |

---

## 🧾 Sample Request Body

{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 28,
  "department": "IT"
}

---

## 💡 Future Improvements

- JWT Authentication  
- Docker Support  
- PostgreSQL Integration  
- Async APIs  
- Unit Testing  

---

## 👨‍💻 Author

Kamesh Rathore  

