# tamise-backend

Ce dépôt contient le code source du backend de l'application de commande de plats et boissons en utilisant FastAPI, PostgreSQL et SQLAlchemy.

## Fonctionnalités

- Gestion des plats du menu, avec leur nom, prix, image et ingrédients.
- Gestion des boissons du menu, avec leur nom, prix et image.
- Passage de commandes, avec la possibilité de choisir des plats, retirer des ingrédients, ajouter des boissons, etc.
- Suivi des commandes, avec des statuts tels que "en attente", "en préparation", "prête", etc.
- Stockage des données dans une base de données PostgreSQL.
- Utilisation de SQLAlchemy pour l'interaction avec la base de données.

## Prérequis

Avant de pouvoir exécuter le backend, assurez-vous d'avoir installé les éléments suivants :

- Python
- Poetry

Configurer le .env pour communiquer avec la BDD

## Installation

1. Clonez ce dépôt sur votre machine.

```bash
git clone https://github.com/ybenannoune/tamise-backend.git
```

2. poetry install

3. poetry run app
