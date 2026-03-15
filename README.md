# Cosmos Quiz (scaffold)

## Démarrage rapide
1. Copier `.env.example` vers `.env` et ajuster les clés.
2. Lancer la stack : `docker-compose up --build`.

## Frontend (local)
```
cd frontend
npm install
npm run dev
```

## Backend (local)
```
cd backend
.venv\\Scripts\\python -m pip install -r requirements.txt
.venv\\Scripts\\python manage.py migrate
.venv\\Scripts\\python manage.py runserver
```
