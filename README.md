<h1 align="center">CO5G Ecommerce API</h1>
<h3 align='center'>Software Engineer | AI, ML, DL & Computer Vision</h3>

<p align="center">
  <!-- Badges -->
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-0.115.12-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white">
</p>

---

## Descipción

API backend para un sistema de ecommerce básico desarrollada con FastAPI.  
Incluye autenticación JWT, gestión de usuarios y base para CRUD de productos.

---

## Stack Tecnológico

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT (python-jose)
- Docker & Docker Compose

---

## Configuración del entorno

Clonar el repositorio:

```bash
git clone https://github.com/hpmezam/co5g-ecommerce-api.git
cd co5g-ecommerce-api
````
Crear archivo .env basado en .env.example:
```bash
cp .env.example .env
````

---

## Ejecución
```bash
docker-compose up --build
````
La API estará disponible en:
```bash
http://localhost:8000
````
Documentación Swagger:
```bash
http://localhost:8000/docs
````
---
## Autenticación
La API utiliza JWT (Bearer Token).

Endpoints disponibles:

Registro
```bash
POST /auth/register
````
Login
```bash
POST /auth/login
````
Respuesta
```bash
{
  "access_token": "TOKEN",
  "token_type": "bearer"
}
````
Usuario autenticado
```bash
GET /auth/me
````
Requiere header:
```bash
Authorization: Bearer <TOKEN>
````
---
## Estructura del proyecto
```bash
app/
├── routes/
├── models/
├── schemas/
├── services/
├── database/
├── auth/
├── utils/
└── main.py
````

---

## Seguridad implementada

- Hash de contraseñas con bcrypt
- Autenticación JWT
- Validación de datos con Pydantic
- JWT (python-jose)
- Variables de entorno (.env)
- Manejo de errores HTTP

---

## Autor

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
