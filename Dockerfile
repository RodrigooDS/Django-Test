# Imagen base
FROM python:3.11.3

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /code

# Instalar dependencias del sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gettext \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar y instalar dependencias de Python
COPY pyproject.toml poetry.lock /code/
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copiar el código fuente de Django
COPY . /code/

# Puerto expuesto por la aplicación
EXPOSE 8001

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]