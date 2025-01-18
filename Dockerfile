# Usar una imagen base de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo requirements.txt y el script al contenedor
COPY requirements.txt ./
COPY .env ./
COPY script.py ./

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar el script al iniciar el contenedor
CMD ["python", "script.py"]
