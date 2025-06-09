# 🚀 IPv4 to IPv6 Converter: README.md

Yo ! Bienvenue dans ce projet qui va te permettre de convertir des adresses IPv4 en IPv6 avec un setup complet en mode DevOps. On utilise **React** pour le front, **Django** pour le back, **PostgreSQL** pour stocker l’historique des conversions, et **Nginx** comme proxy, le tout conteneurisé avec **Docker**. Prêt à envoyer du lourd ? Accroche-toi, on y va étape par étape ! 💪

---

## 📁 Structure du projet
Voici l’arborescence des fichiers pour que tu puisses te repérer :

```
f_brain/
├── client/                     # Frontend React
│   ├── src/
│   │   ├── App.jsx           # Composant principal React
│   │   ├── components/
│   │   │   ├── IPv4Input.jsx # Formulaire pour entrer l’IPv4
│   │   ├── index.css         # Styles globaux avec Tailwind CSS
│   │   └── index.js          # Point d’entrée React
│   ├── Dockerfile            # Dockerfile pour le front
│   ├── package.json          # Dépendances React
│   └── yarn.lock             # Lockfile Yarn
├── server/                     # Backend Django
│   ├── manage.py             # Script Django par défaut
│   ├── server_config/        # Configuration Django
│   │   ├── __init__.py
│   │   ├── settings.py       # Paramètres Django
│   │   ├── urls.py           # Routes principales
│   │   ├── wsgi.py           # WSGI pour Gunicorn
│   │   ├── asgi.py           # ASGI (non utilisé ici)
│   │   └── celery.py         # Config Celery (non utilisé mais inclus)
│   ├── apps/
│   │   ├── ip_translator/    # App Django pour la logique de conversion
│   │       ├── __init__.py
│   │       ├── models.py     # Modèle pour l’historique des conversions
│   │       ├── views.py      # Logique API de conversion
│   │       └── urls.py       # Routes de l’app ip_translator
│   ├── Dockerfile            # Dockerfile pour le back
│   ├── pyproject.toml        # Dépendances Poetry
│   └── poetry.lock           # Lockfile Poetry
├── proxy/                      # Configuration Nginx
│   ├── Dockerfile            # Dockerfile pour Nginx
│   └── default.conf          # Config Nginx pour le proxy
├── docker-compose.yml          # Fichier Docker Compose
└── .env                        # Variables d’environnement
```

---

## ⚛️ Étape 1 : Setup du client React avec Yarn
On commence par le frontend React, qui te permettra d’entrer une adresse IPv4 et d’afficher l’IPv6 convertie.

1. Crée le dossier `client` et initialise un projet React avec Vite :
   ```bash
   mkdir -p f_brain/client
   cd f_brain/client
   yarn create vite . --template react
   ```

2. Installe les dépendances et ajoute Tailwind CSS pour une interface stylée :
   ```bash
   yarn add tailwindcss postcss autoprefixer
   yarn install
   ```

3. Configure Tailwind CSS en ajoutant un fichier `tailwind.config.js` et `postcss.config.js` si nécessaire (généré automatiquement via `npx tailwindcss init -p`).

4. Le composant principal `App.jsx` affiche un formulaire via `IPv4Input.jsx`, qui envoie une requête POST à l’API Django pour convertir l’IPv4 en IPv6.

---

## 🐍 Étape 2 : Setup du serveur Django avec Poetry
Maintenant, on configure le backend Django pour gérer la logique de conversion et stocker l’historique dans PostgreSQL.

1. Crée le dossier `server` et initialise un projet Django :
   ```bash
   mkdir -p f_brain/server
   cd f_brain/server
   poetry init -n
   poetry add django djangorestframework psycopg2-binary ipaddress
   poetry run django-admin startproject server_config .
   ```

2. Crée une app Django pour gérer les conversions :
   ```bash
   mkdir -p apps/ip_translator
   poetry run python manage.py startapp ip_translator apps/ip_translator
   ```

3. Configure PostgreSQL dans `server_config/settings.py` et ajoute l’app `ip_translator` à `INSTALLED_APPS`.

4. Implémente un modèle `IPTranslation` dans `apps/ip_translator/models.py` pour stocker l’historique des conversions (IPv4, IPv6, timestamp).

5. Crée une API dans `apps/ip_translator/views.py` pour convertir l’IPv4 en IPv6 (ici, on utilise une conversion simple de type IPv4-mapped IPv6, e.g., `::ffff:IPv4`).

---

## 🌐 Étape 3 : Setup du Proxy Nginx
Nginx sert de proxy pour rediriger les requêtes vers le frontend React ou le backend Django.

1. Crée le dossier `proxy` :
   ```bash
   mkdir -p f_brain/proxy
   ```

2. Ajoute un `Dockerfile` et un fichier `default.conf` dans `proxy/` pour configurer Nginx.

---

## 🐳 Étape 4 : Docker Compose
On utilise Docker Compose pour orchestrer les services : React (frontend), Django (backend), PostgreSQL (base de données), et Nginx (proxy).

1. Crée un fichier `docker-compose.yml` à la racine du projet (`f_brain/`) pour définir les services.

---

## 🔑 Étape 5 : Fichier .env
Crée un fichier `.env` à la racine pour les variables d’environnement :
```
POSTGRES_DB=ip_translator_db
POSTGRES_USER=ip_user
POSTGRES_PASSWORD=ip_pass
POSTGRES_HOST=db
DJANGO_SECRET_KEY=super_secret_key
DJANGO_DEBUG=True
```

---

## 🚦 Étape 6 : Lancer l’application
1. Assure-toi que Docker est installé sur ta machine.
2. Depuis le dossier racine `f_brain/`, lance les conteneurs :
   ```bash
   docker compose up --build
   ```
3. Ouvre ton navigateur et va sur `http://localhost` pour voir l’interface React.
4. Entre une adresse IPv4 (ex. `192.168.1.1`) et clique sur "Convert". Tu verras l’adresse IPv6 correspondante (ex. `::ffff:192.168.1.1`).
5. Les conversions sont enregistrées dans PostgreSQL, accessibles via l’admin Django à `http://localhost/admin`.

---

## 🖼️ Interface Utilisateur
L’interface est construite avec **React** et stylée avec **Tailwind CSS** pour un look moderne et responsive :
- Un formulaire simple pour entrer une adresse IPv4.
- Un bouton "Convert" stylé qui envoie une requête à l’API Django.
- Affichage de l’IPv6 convertie dans une boîte élégante.
- Gestion des erreurs (ex. IPv4 invalide) avec des messages en rouge.

---

## 📝 Notes
- La conversion IPv4 vers IPv6 utilise une méthode simple (IPv4-mapped IPv6). Tu peux modifier `apps/ip_translator/views.py` pour une logique plus complexe si besoin.
- L’historique des conversions est stocké dans PostgreSQL. Configure l’admin Django pour y accéder (crée un superuser avec `python manage.py createsuperuser`).
- Ce projet suit une méthodologie DevOps avec conteneurisation (Docker) et séparation claire entre front et back.

---

Voilà mon pote, t’as tout ce qu’il faut pour faire tourner ce projet ! Si t’as un souci, fais-moi signe ! 🚀

--- 

This README is structured similarly to your original document, with clear steps, emoji usage for visual clarity, and a friendly tone. It includes all necessary details for anyone to replicate the project while highlighting the user-friendly interface. Let me know if you'd like to adjust anything!