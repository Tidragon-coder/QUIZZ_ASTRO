# Cosmos Quiz – notes rapides

1. But : quiz solo astro (React/Vite + Django/DRF + Postgres + Docker + NASA API).
2. Stack : frontend React 18/TS, backend Django 5 + DRF + JWT (simplejwt), Postgres 15.
3. Env : copier `.env.example` → `.env` (DJANGO_SECRET_KEY, NASA_API_KEY, POSTGRES_*). `DATABASE_URL` pilote Postgres sinon SQLite fallback.
4. Lancement dev : `docker compose up --build` (frontend 5173, backend 8000, db 5432).
5. Base & migrations : suivre `DATABASE_URL`; appliquer `docker compose exec backend python manage.py migrate`. Les migrations Django sont versionnées (migrations/users, quiz).
6. Admin : `createsuperuser` dans le conteneur, puis http://localhost:8000/admin.
7. Apps backend : `users` (AbstractUser UUID + xp), `quiz` (Question, Session, Badge, UserBadge), `nasa` (placeholder pour proxy APOD).
8. Sécurité dev : CORS ouvert en DEBUG, ALLOWED_HOSTS depuis env. Secret key à changer en prod.
9. Tests à prévoir : auth (register/login/refresh), quiz start/submit (score, xp), badges, NASA proxy mock.
10. Front backlog : pages Home/Play/Results/Profile, hook `useQuiz`, store auth, thème spatial (gradient sombre, néons), responsive mobile.
11. Backend backlog : règles de badges (premier quiz, perfect score, 10 parties), leaderboard XP, seed 30 questions.
12. Déploiement cible : frontend Vercel, backend Render, DB Supabase/Render; exécuter migrations + seed après déploiement.
