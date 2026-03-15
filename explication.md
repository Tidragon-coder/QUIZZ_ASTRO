# Cosmos Quiz — Résumé complet du projet

## Vue d'ensemble

Cosmos Quiz est une application web de quiz solo sur le thème de l'astronomie. L'utilisateur crée un compte, choisit une catégorie et une difficulté, répond à des questions en temps limité, accumule de l'XP et débloque des badges. L'interface utilise les images de l'API NASA pour créer une expérience visuelle immersive.

---

## Stack technique

### Frontend
- **React 18** avec **TypeScript**
- **Vite** comme bundler
- **React Router v6** pour la navigation
- **Axios** pour les appels API (typé avec des interfaces TS)
- **CSS Modules** ou **Tailwind CSS** pour le style

### Backend
- **Django 5** + **Django REST Framework (DRF)**
- **djangorestframework-simplejwt** pour l'authentification JWT
- **Django Admin** pour la gestion du contenu (questions, badges, utilisateurs)
- **django-cors-headers** pour autoriser les appels depuis le frontend

### Base de données
- **PostgreSQL 15**
- Géré via l'ORM Django (migrations automatiques)

### Infra / DevOps
- **Docker** + **Docker Compose** pour tout orchestrer
- 3 services : `frontend`, `backend`, `db`
- Fichier `.env` pour les variables d'environnement

### API externe
- **NASA API** (gratuite) — deux endpoints utilisés :
  - `APOD` (Astronomy Picture of the Day) : image spatiale du jour comme fond de quiz
  - `Images & Video Library` : images pour illustrer les questions
  - Clé `DEMO_KEY` suffisante pour commencer, clé gratuite sur api.nasa.gov

---

## Structure des dossiers

```
cosmos-quiz/
├── docker-compose.yml
├── .env
├── frontend/
│   ├── Dockerfile
│   ├── vite.config.ts
│   ├── src/
│   │   ├── components/
│   │   │   ├── Quiz/
│   │   │   │   ├── QuestionCard.tsx
│   │   │   │   ├── Timer.tsx
│   │   │   │   └── AnswerFeedback.tsx
│   │   │   ├── Profile/
│   │   │   │   ├── Dashboard.tsx
│   │   │   │   └── BadgeList.tsx
│   │   │   └── UI/
│   │   │       ├── Navbar.tsx
│   │   │       └── StarBackground.tsx
│   │   ├── pages/
│   │   │   ├── Home.tsx
│   │   │   ├── Play.tsx
│   │   │   ├── Results.tsx
│   │   │   └── Profile.tsx
│   │   ├── hooks/
│   │   │   ├── useTimer.ts
│   │   │   └── useQuiz.ts
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── store/
│   │   │   └── authStore.ts
│   │   └── types/
│   │       └── index.ts
└── backend/
    ├── Dockerfile
    ├── requirements.txt
    ├── manage.py
    ├── config/
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── apps/
        ├── users/
        │   ├── models.py
        │   ├── serializers.py
        │   ├── views.py
        │   └── urls.py
        ├── quiz/
        │   ├── models.py
        │   ├── serializers.py
        │   ├── views.py
        │   └── urls.py
        └── nasa/
            ├── service.py
            └── views.py
```

---

## Modèle de base de données (Django ORM)

### User (extension de AbstractUser)
| Champ | Type |
|---|---|
| id | UUID (PK) |
| username | CharField |
| email | EmailField |
| password | CharField (hashé) |
| xp | IntegerField (défaut: 0) |
| created_at | DateTimeField |

### Question
| Champ | Type |
|---|---|
| id | UUID (PK) |
| text | TextField |
| options | JSONField (liste de 4 choix) |
| answer | CharField (la bonne réponse) |
| category | CharField (planètes, étoiles, missions…) |
| difficulty | CharField (easy / medium / hard) |
| image_url | URLField (optionnel) |
| explanation | TextField (anecdote affichée après réponse) |

### Session
| Champ | Type |
|---|---|
| id | UUID (PK) |
| user | ForeignKey → User |
| score | IntegerField |
| total_questions | IntegerField |
| category | CharField |
| difficulty | CharField |
| played_at | DateTimeField |

### Badge
| Champ | Type |
|---|---|
| id | UUID (PK) |
| slug | CharField (ex: "first-game", "perfect-score") |
| name | CharField |
| description | TextField |
| icon | CharField (emoji ou nom d'icône) |

### UserBadge
| Champ | Type |
|---|---|
| id | UUID (PK) |
| user | ForeignKey → User |
| badge | ForeignKey → Badge |
| unlocked_at | DateTimeField |

---

## Endpoints API REST

### Auth
| Méthode | Route | Description |
|---|---|---|
| POST | `/api/auth/register/` | Inscription |
| POST | `/api/auth/login/` | Connexion → retourne access + refresh JWT |
| POST | `/api/auth/refresh/` | Rafraîchir le token |

### Quiz
| Méthode | Route | Description |
|---|---|---|
| GET | `/api/quiz/start/?category=&difficulty=` | Retourne 10 questions aléatoires |
| POST | `/api/quiz/submit/` | Soumet les réponses, calcule le score, sauvegarde la session, attribue l'XP |

### Utilisateur
| Méthode | Route | Description |
|---|---|---|
| GET | `/api/user/profile/` | XP, badges débloqués, historique sessions |
| GET | `/api/leaderboard/` | Top 10 utilisateurs par XP |

### NASA (proxy backend)
| Méthode | Route | Description |
|---|---|---|
| GET | `/api/nasa/apod/` | Photo NASA du jour (la clé API reste côté serveur) |

---

## Docker Compose

```yaml
services:
  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    depends_on:
      - backend

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    volumes:
      - ./backend:/app
    environment:
      - DATABASE_URL=postgres://cosmos:cosmos@db:5432/cosmos_db
      - NASA_API_KEY=${NASA_API_KEY}
      - SECRET_KEY=${DJANGO_SECRET_KEY}
      - DEBUG=True
    depends_on:
      - db

  db:
    image: postgres:15
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=cosmos
      - POSTGRES_PASSWORD=cosmos
      - POSTGRES_DB=cosmos_db
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

## Fichier .env à créer à la racine

```
DJANGO_SECRET_KEY=une_cle_secrete_longue_et_aleatoire
NASA_API_KEY=DEMO_KEY
POSTGRES_USER=cosmos
POSTGRES_PASSWORD=cosmos
POSTGRES_DB=cosmos_db
```

---

## Fonctionnalités à développer

### MVP (à faire en priorité)
- Inscription / connexion avec JWT
- Quiz solo : choix catégorie + difficulté, 10 questions, timer, score
- Explication affichée après chaque réponse
- Sauvegarde de la session en base
- Profil utilisateur avec XP et historique
- Image NASA du jour en fond via APOD

### Extensions (après le MVP)
- Système de badges (premier quiz, score parfait, 10 parties jouées…)
- Leaderboard global
- Mode "défi du jour" (mêmes questions pour tout le monde pendant 24h)
- Responsive mobile

---

## Plan de développement (4 semaines)

### Semaine 1 — Backend core
- Setup Django + DRF + PostgreSQL sous Docker
- Modèles User, Question, Session, Badge
- Auth JWT (register, login, refresh)
- Endpoints quiz/start et quiz/submit fonctionnels
- Seed de 30 questions en dur via une fixture JSON
- Django Admin configuré pour gérer les questions

### Semaine 2 — Frontend quiz
- Setup React + TypeScript + Vite sous Docker
- Routing : Home, Play, Results, Profile
- Composants QuestionCard, Timer, AnswerFeedback
- Connexion aux endpoints backend (auth + quiz)
- Gestion du token JWT en localStorage

### Semaine 3 — Profil + NASA API
- Page profil : XP, historique, badges
- Proxy backend vers NASA APOD
- Affichage de la photo NASA comme fond de quiz
- Système de badges côté backend

### Semaine 4 — Polish + déploiement
- Animations et transitions
- Responsive mobile
- Leaderboard
- Déploiement : Vercel (frontend), Render (backend), Supabase free (PostgreSQL)

---

## Déploiement en production (gratuit)

| Service | Plateforme | Tier |
|---|---|---|
| Frontend | Vercel | Free |
| Backend Django | Render | Free (cold start ~30s) |
| PostgreSQL | Supabase ou Render PostgreSQL | Free (500MB) |
| NASA API | api.nasa.gov | Free (1000 req/h) |

---

## Commandes utiles

```bash
# Lancer le projet en local
docker-compose up --build

# Créer les migrations Django
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate

# Créer un superuser pour Django Admin
docker-compose exec backend python manage.py createsuperuser

# Charger les questions de seed
docker-compose exec backend python manage.py loaddata questions.json

# Accéder à Django Admin
http://localhost:8000/admin
```