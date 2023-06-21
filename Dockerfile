FROM arm64v8/python:3.11-slim

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Installation de Poetry
RUN pip install poetry

# Copie des fichiers de dépendances
COPY pyproject.toml poetry.lock ./

# Installation des dépendances du projet
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-dev

# Copie des fichiers de l'application
COPY . .

# Exposition du port
EXPOSE 8000

# Commande d'exécution de l'application
CMD ["poetry", "run", "app"]
