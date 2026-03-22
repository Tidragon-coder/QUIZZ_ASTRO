# Cosmos Quiz

## Démarrage rapide (Docker)
1. Copier `.env.example` en `.env` et renseigner les clés (`DJANGO_SECRET_KEY`, `NASA_API_KEY`...).
2. Lancer la stack : `docker compose up --build`.
3. Appliquer les migrations Postgres : `docker compose exec backend python manage.py migrate`.
4. Créer un superuser : `docker compose exec -it backend python manage.py createsuperuser`.
5. Admin : http://localhost:8000/admin • Frontend : http://localhost:5173

## Backend (hors Docker, SQLite ou DATABASE_URL)
```
cd backend
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
set DATABASE_URL=postgres://cosmos:cosmos@localhost:5432/cosmos_db   # optionnel
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

## Frontend (hors Docker)
```
cd frontend
npm install
npm run dev
```
