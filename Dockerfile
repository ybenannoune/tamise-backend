FROM arm64v8/python:3.10-slim-buster as requirements-stage
WORKDIR /tmp
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM arm64v8/python:3.10-slim-buster

WORKDIR /app

#Copy the requirements.txt file to the /code directory.
#This file only lives in the previous Docker stage, that's why we use --from-requirements-stage to copy it.
COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

# Install the package dependencies in the generated requirements.txt file.
RUN python -m pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copie des fichiers de l'application
COPY . .

# Commande d'exécution de l'application
CMD ["uvicorn", "tamise.main:app", "--host", "0.0.0.0", "--port", "8000","--proxy-headers","--root-path=/api"]