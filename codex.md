1. Vue d'ensemble : Cosmos Quiz = app web de quiz solo astro (React/Vite + Django/DRF + Postgres + Docker + NASA API).
2. Choix du workflow : travailler en conteneurs Docker (services frontend, backend, db) pour dev/CI homogènes.
3. Préparer l'environnement : créer `.env` racine avec DJANGO_SECRET_KEY, NASA_API_KEY, POSTGRES_USER/PASSWORD/DB.
4. Lancer la stack de base pour vérif : `docker-compose up --build` (frontend 5173, backend 8000, db 5432).
5. Backend/Semaine1 objectif : mettre en place Django 5 + DRF + JWT + modèles + endpoints quiz + admin.
6. Backend 1/Init : générer projet Django, configurer `config/settings.py` (INSTALLED_APPS DRF, cors, simplejwt, postgres).
7. Backend 2/DB : configurer Postgres via env DATABASE_URL, appliquer migrations initiales.
8. Backend 3/Auth : ajouter app users (AbstractUser custom), modèles champs xp/created_at, serializer + views register/login/refresh (simplejwt).
9. Backend 4/Quiz modèles : Question (uuid, text, options JSON, answer, category, difficulty, image_url, explanation), Session (user FK, score, total_questions, category, difficulty, played_at).
10. Backend 5/Badges : modèles Badge (slug, name, description, icon), UserBadge (user FK, badge FK, unlocked_at) même si activé S3 ou en extension.
11. Backend 6/Endpoints quiz : GET `/api/quiz/start/?category=&difficulty=` renvoie 10 questions random filtrées; POST `/api/quiz/submit/` calcule score, enregistre Session, renvoie feedback + XP gagné.
12. Backend 7/NASA proxy : vue `/api/nasa/apod/` qui appelle API NASA avec clé serveur, met en cache court.
13. Backend 8/Admin : activer Django Admin, enregistrer User, Question, Session, Badge, UserBadge; config listes/filters/search.
14. Backend 9/Seed : créer fixture `questions.json` (~30 entrées) et commande `loaddata` pour remplir la base.
15. Backend 10/CORS : config `django-cors-headers` pour autoriser frontend (localhost:5173).
16. Backend 11/Tests : ajouter tests DRF pour auth, quiz/start, quiz/submit (scoring, XP), NASA proxy (mock).
17. Frontend/Semaine2 objectif : scaffolder React 18 + TS + Vite, router, pages Home/Play/Results/Profile.
18. Frontend 1/Structure : créer arborescence `src/components/Quiz`, `Profile`, `UI`, `pages`, `hooks`, `services`, `store`, `types`.
19. Frontend 2/Routing : config React Router v6 pour `/`, `/play`, `/results`, `/profile`.
20. Frontend 3/Auth : vue Login/Register, stockage JWT en localStorage, intercepteur Axios pour Authorization bearer + refresh.
21. Frontend 4/API client : `services/api.ts` typé TS pour auth, quiz/start, quiz/submit, profile, leaderboard, nasa/apod.
22. Frontend 5/Quiz flow : hook `useQuiz` (fetch start, timer start, submit answers), composant `QuestionCard`, `Timer`, `AnswerFeedback`.
23. Frontend 6/State : store léger (zustand ou contexte) pour user/auth/token + session courante.
24. Frontend 7/UI : `Navbar`, `StarBackground` consommant APOD en fond (fallback statique si erreur).
25. Frontend 8/Pages : Home (CTA jouer), Play (question courante, options, timer, feedback), Results (score, explication, XP), Profile (XP, historique, badges).
26. Frontend 9/Styles : choisir CSS Modules ou Tailwind; définir thème spatial (dégradés sombres, néons, typo display).
27. Frontend 10/Tests : tests unitaires hooks et composants critiques (Timer, AnswerFeedback), e2e basiques si temps.
28. Intégration/Semaine3 objectif : profil complet, badges, NASA proxy, historique.
29. Intégration 1/Profil API : GET profile renvoie xp, badges débloqués, dernières sessions; côté front afficher cartes badges + timeline sessions.
30. Intégration 2/Badges règles : implémenter logique (premier quiz, perfect score, 10 parties jouées), attribuer dans quiz/submit.
31. Intégration 3/NASA : connecter front au proxy APOD, rafraîchir fond quotidien, gérer loading/erreurs.
32. Intégration 4/Leaderboard : endpoint `/api/leaderboard/` (top 10 XP), composant tableau front.
33. Intégration 5/Accessibilité : focus states, couleurs contrastées, navigation clavier sur questions.
34. Finition/Semaine4 objectif : polish UI, responsive, perf, déploiement gratuit.
35. Finition 1/Animations : transitions entre questions, micro-interactions boutons, skeletons loading.
36. Finition 2/Responsive : breakpoints mobile/desktop; tester sur viewport 360px+.
37. Finition 3/Sécurité : limiter CORS, HTTPS en prod, cookies secure si passage, rate-limit endpoints publics.
38. Finition 4/Perf : cache APOD, compression assets, lazy load images/questions.
39. Finition 5/Monitoring : logs DRF, capturing erreurs front (Sentry optionnel free).
40. Déploiement : Vercel (frontend), Render free (backend), Supabase/Render Postgres; stocker secrets env séparés.
41. Déploiement 1/Builds : Dockerfile frontend (npm ci, build, preview), backend (pip install -r requirements.txt, collectstatic si besoin).
42. Déploiement 2/Migrations : exécuter `migrate` et `loaddata` sur Render après déploiement.
43. Déploiement 3/Domaines : config URLs Vercel → backend Render, CORS + ALLOWED_HOSTS.
44. Données & contenu : rédiger 30 questions initiales multi-difficulté + images NASA (URL), vérifier droits (API libre).
45. Documentation : README usage, commandes docker, endpoints API, schéma DB, checklist déploiement.
46. Qualité continue : ajouter CI simple (lint + tests backend/frontend) via GitHub Actions si repo public.
47. Backlog futur : mode défi du jour, multi-langues, notifications e-mail, OAuth social, analytics basiques.
