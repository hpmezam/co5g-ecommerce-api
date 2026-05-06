FROM python:3.12-slim

# Evitar comprobaciones innecesarias
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONUNBUFFERED=1

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivo de dependencias
COPY requirements.txt . 

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto en el que la aplicación correrá
EXPOSE 8000

# Ejecutar FastAPI (modo dev)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]