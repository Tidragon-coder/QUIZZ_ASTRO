# Cosmos Quiz – résumé projet

## Idée
Application de quiz solo sur l’astronomie : l’utilisateur choisit catégorie/difficulté, répond à 10 questions, gagne de l’XP et débloque des badges. Visuel alimenté par l’API NASA (APOD).

## Stack
- Frontend : React 18 + TypeScript + Vite, React Router v6, Axios, CSS Modules ou Tailwind.
- Backend : Django 5, Django REST Framework, simplejwt pour les tokens, django-cors-headers, Postgres via `DATABASE_URL` (fallback SQLite).
- Infra : Docker Compose avec services `frontend`, `backend`, `db` (Postgres 15).

## Données / modèles
- `users.User` : AbstractUser UUID, champs classiques + `xp`, `created_at`.
- `quiz.Question` : UUID, texte, options JSON (4 choix), réponse, catégorie, difficulté, image_url, explication.
- `quiz.Session` : UUID, FK user, score, total_questions, catégorie, difficulté, played_at.
- `quiz.Badge` : UUID, slug unique, nom, description, icône.
- `quiz.UserBadge` : FK user + badge, unique_together, unlocked_at.

## Admin
Les modèles Users/Quiz sont enregistrés dans Django Admin. Créer un superuser dans le conteneur :  
`docker compose exec -it backend python manage.py createsuperuser`

## Démarrage (Docker)
1. Copier `.env.example` → `.env` et renseigner les clés.
2. `docker compose up --build`
3. `docker compose exec backend python manage.py migrate`
4. (option) seed/fixtures quand dispo.
5. Admin : http://localhost:8000/admin • Frontend : http://localhost:5173

## Points de vigilance
- Toujours vérifier que `DATABASE_URL` pointe sur la bonne base avant `migrate`.
- Migrations Django sont versionnées (migrations des apps `users` et `quiz` suivies).
- CORS ouvert seulement en dev (`DEBUG=True`).

## Backlog court terme
- Endpoints REST (auth register/login/refresh, quiz start/submit, profile/leaderboard, proxy NASA APOD).
- Seed ~30 questions multi-difficulté.
- Règles de badges (première partie, perfect score, 10 parties).
- Tests DRF sur auth, quiz, badges, NASA proxy (mock).
