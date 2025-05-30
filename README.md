# FastAPI Vibe Template

A modern, modular FastAPI backend template designed for rapid development with best practices out of the box. This template provides a clean structure for building scalable APIs, featuring SQLAlchemy ORM, Alembic migrations, Poetry dependency management, and Docker-based local development.

---

## Features

- **FastAPI** for high-performance async APIs
- **SQLAlchemy** ORM for database models and queries
- **Alembic** for database migrations
- **Poetry** for dependency management
- **Docker & Docker Compose** for easy local development
- **Modular project structure** for maintainability and clarity
- **Health check endpoints** for service and database
- **Environment-based configuration** via `.env`
- **Ready for extension**: add routers, models, schemas, and more

---

## Tech Stack

- Python 3.12+
- FastAPI
- SQLAlchemy
- Alembic
- Poetry
- Docker & Docker Compose
- PostgreSQL (default, easily swappable)

---

## Directory Structure

```
app/
├── main.py                # App entrypoint, router inclusion, events
├── api/
│   ├── deps.py            # Dependency-injection functions (e.g., DB session)
│   └── routers/
│       └── health.py      # Example health check router
├── crud/                  # CRUD logic per entity (add files as needed)
├── models/                # SQLAlchemy models (add files as needed)
├── schemas/               # Pydantic schemas (add files as needed)
├── database.py            # DB connection/session setup
├── core/
│   ├── config.py          # App settings loaded from .env
│   ├── exceptions.py      # Custom exception handlers (extend as needed)
│   └── security.py        # Security/auth logic (extend as needed)
├── jobs/                  # Background/scheduled tasks
├── middleware/            # Custom middleware
├── tests/                 # Unit/integration tests
├── alembic/               # Alembic migration environment
│   └── versions/          # Migration scripts
├── .env.example           # Example environment variables
├── Dockerfile             # Container build for API
├── docker-compose.yml     # Local dev: API + Postgres
├── alembic.ini            # Alembic config
├── README.md              # This file
```

**See [.clinerules/fastapi_structure.md](.clinerules/fastapi_structure.md) for detailed structure and conventions.**

---

## Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/fastapi_vibe_template.git
cd fastapi_vibe_template
```

### 2. Configure environment variables

Copy the example file and edit as needed:

```bash
cp app/.env.example app/.env
```

Edit `app/.env` to set your project name, version, and database URL.

### 3. Run with Docker (recommended)

```bash
docker-compose up --build
```

- API available at [http://localhost:8000](http://localhost:8000)
- PostgreSQL available at `localhost:5432` (see `docker-compose.yml` for credentials)

### 4. Run locally (with Poetry)

Install dependencies:

```bash
poetry install
```

Start the database (e.g., with Docker):

```bash
docker-compose up db
```

Run the API:

```bash
poetry run uvicorn app.main:app --reload
```

---

## Environment Variables

Set in `app/.env` (see `app/.env.example`):

- `PROJECT_NAME` – Name of your project (used in docs/UI)
- `VERSION` – API version string
- `DATABASE_URL` – SQLAlchemy DB URL (default: Postgres for Docker Compose)

---

## Database Migrations

This template uses Alembic for migrations.

**Create a new migration:**
```bash
poetry run alembic revision --autogenerate -m "your message"
```

**Apply migrations:**
```bash
poetry run alembic upgrade head
```

Migration scripts are in `app/alembic/versions/`.

---

## Health Check Endpoints

- `GET /health/service` – Service health (always returns `{"status": "ok"}`)
- `GET /health/db` – Database health (checks DB connection)

---

## How to Extend

- **Add new routers:** Create a new file in `app/api/routers/` and include it in the main router.
- **Add models:** Create a new file in `app/models/` for each entity.
- **Add schemas:** Create a new file in `app/schemas/` for each domain/entity.
- **Add CRUD logic:** Create a new file in `app/crud/` per entity.
- **Add dependencies:** Use `app/api/deps.py` for shared dependencies (e.g., DB session).
- **Add background jobs:** Place scripts in `app/jobs/`.
- **Add middleware:** Place modules in `app/middleware/` and register in `main.py`.

**Follow the conventions in [.clinerules/fastapi_structure.md](.clinerules/fastapi_structure.md) for modularity and maintainability.**

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Author

Created by [dromi](mailto:hello@finechariot.com).
