<h1 align="center">CO5G Ecommerce API</h1>
<h3 align="center">Software Engineer | AI, ML, DL & Computer Vision</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-0.115.12-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white">
</p>

---

## Description

Backend API for a basic ecommerce system built with FastAPI.  
Includes JWT authentication, user management, and product CRUD operations.

---

## Technology Stack

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication (python-jose)
- Docker & Docker Compose
- Pydantic
- bcrypt

---

## Project Structure

```bash
app/
├── auth/
├── core/
├── database/
├── models/
├── routes/
├── schemas/
├── services/
└── main.py
```

---

## Environment Configuration

Clone the repository:

```bash
git clone https://github.com/hpmezam/co5g-ecommerce-api.git
cd co5g-ecommerce-api
```

Create the `.env` file from `.env.example`:

```bash
# Windows CMD
copy .env.example .env
# Linux / macOS
cp .env.example .env
```

---

## Environment Variables

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=ecommerce

POSTGRESQL_USERNAME=postgres
POSTGRESQL_PASSWORD=postgres
POSTGRESQL_DATABASE=ecommerce
POSTGRESQL_SERVER=db
POSTGRESQL_PORT=5432

SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret_key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## Running the Project

Build and start the containers:

```bash
docker-compose up --build
```

The API will be available at:

```bash
http://localhost:8000
```

Swagger documentation:

```bash
http://localhost:8000/docs
```

ReDoc documentation:

```bash
http://localhost:8000/redoc
```

---

## Authentication

The API uses JWT Bearer Authentication.

### Available Endpoints

Register user:

```bash
POST /auth/register
```

Login:

```bash
POST /auth/login
```

Authenticated user:

```bash
GET /auth/me
```

### Login Response

```json
{
  "access_token": "TOKEN",
  "token_type": "bearer"
}
```

### Authorization Header

```bash
Authorization: Bearer <TOKEN>
```

---

## Products Endpoints

Protected endpoints require JWT authentication.

```bash
POST   /products
GET    /products
GET    /products/{id}
PUT    /products/{id}
DELETE /products/{id}
```

---

## Example Product Payload

```json
{
  "name": "Laptop Gamer ASUS",
  "description": "Ryzen 7, 16GB RAM, RTX 4060",
  "price": 1499.99,
  "stock": 10
}
```

---

## Implemented Security

- Password hashing with bcrypt
- JWT Authentication
- Request validation with Pydantic
- Environment variables support
- HTTP exception handling
- Database constraints validation

---

## Features

- User Registration
- User Login
- JWT Authentication
- Product CRUD
- PostgreSQL Integration
- SQLAlchemy ORM
- Dockerized Environment
- Interactive Swagger Documentation

---

## Author

Ing. Henry Meza

<br>

<div align="center">

  <a href="https://github.com/hpmezam">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="GitHub">
  </a>

  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">

  <a href="https://www.linkedin.com/in/hpmezam/">
    <img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="LinkedIn">
  </a>

  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">

  <a href="https://www.tiktok.com/@deepvisionh2m">
    <img src="https://cdn-icons-png.flaticon.com/512/3046/3046121.png" width="3%" alt="TikTok">
  </a>
  
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">

</div>
