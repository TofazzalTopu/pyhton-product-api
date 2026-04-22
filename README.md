# 🚀 FastAPI Product API

A production-ready FastAPI application implementing a layered architecture (Controller → Service → Repository → Model) with MySQL integration.

---

## 📌 Features

* ✅ FastAPI REST API
* ✅ Layered architecture (clean separation of concerns)
* ✅ MySQL + SQLAlchemy ORM
* ✅ Pydantic DTO validation
* ✅ Environment-based configuration (`.env`)
* ✅ Production-ready structure
* ✅ Hot reload for development

---

## 🏗️ Project Structure

```
fastapi-app/
│
├── app/
│   ├── main.py                # Entry point
│   ├── core/
│   │   └── database.py        # DB config
│   ├── api/
│   │   └── product_controller.py
│   ├── service/
│   │   └── product_service.py
│   ├── repository/
│   │   └── product_repository.py
│   ├── model/
│   │   └── product_model.py
│   └── dto/
│       └── product_dto.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd fastapi-app
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

---

### 3. Activate Virtual Environment

#### macOS / Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 5. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=mysql+pymysql://root:password@127.0.0.1:3306/yourdb
```

⚠️ Use `127.0.0.1` instead of `localhost` for MySQL connections.

---

## ▶️ Run Application

```bash
uvicorn app.main:app --reload
```

App will be available at:

👉 http://127.0.0.1:8000
👉 Swagger UI: http://127.0.0.1:8000/docs

---

## 🧪 API Endpoints

### Product APIs

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /products      | Get all products  |
| GET    | /products/{id} | Get product by ID |
| POST   | /products      | Create product    |
| PUT    | /products/{id} | Update product    |
| DELETE | /products/{id} | Delete product    |

---

## 🗄️ Database

* MySQL
* ORM: SQLAlchemy
* Driver: PyMySQL

---

## ⚠️ Common Issues & Fixes

### ❌ MySQL Connection Refused

**Error:**

```
Can't connect to MySQL server on 'localhost'
```

**Fix:**

* Ensure MySQL is running
* Use `127.0.0.1` instead of `localhost`
* Verify port `3306`

---

## 📦 Requirements

Example `requirements.txt`:

```
fastapi
uvicorn
sqlalchemy
pymysql
python-dotenv
```

---

## 🐳 Docker Support (Optional)

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🧠 Best Practices

* Use `.env` for configuration
* Follow layered architecture
* Keep controllers thin (business logic in service layer)
* Use DTOs for validation
* Add retry logic for DB in production

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Md Tofazzal Hossain
Java Developer | Backend Engineer
