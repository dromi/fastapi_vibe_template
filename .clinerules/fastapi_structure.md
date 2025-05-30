# FastAPI Project Structure – Specification for AI Agents & Contributors

This document specifies the folder and file structure, naming conventions, and organizational logic for the FastAPI project. It is intended for human developers and AI coding agents to understand exactly how to organize and extend the codebase.

---

## 1. **Project Overview**

This project is built on [FastAPI](https://fastapi.tiangolo.com/) and uses SQLAlchemy for ORM and Alembic for migrations. It is designed for modularity, maintainability, and clarity. Each folder serves a single, clearly defined purpose.

---

## 2. **Folder & File Structure**

**Project root:**

```
app/
├── main.py
├── api/
│   ├── __init__.py
│   ├── deps.py
│   └── routers/
│       └── __init__.py
├── crud/
│   └── __init__.py
├── models/
│   └── __init__.py
├── schemas/
│   └── __init__.py
├── database.py
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── alembic.ini
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── exceptions.py
│   └── security.py
├── jobs/
│   └── __init__.py
├── middleware/
│   └── __init__.py
├── tests/
│   └── __init__.py
README.md
.env.example
Dockerfile
docker-compose.yml
.gitignore
```

---

## 3. **Folder Responsibilities**

* **main.py**
  App entrypoint. Creates the FastAPI app, includes routers, and configures startup/shutdown events.

* **api/**
  Contains all API routing logic and dependencies.

  * **deps.py:** All dependency-injection functions (e.g., for DB session, auth, etc.).
  * **routers/:** Contains APIRouter modules grouped by domain/feature (create a file per route group as needed).

* **crud/**
  Contains files with CRUD (Create, Read, Update, Delete) functions for each database entity/table.
  Each entity/table should have its own file (e.g., `crud/item.py`), but initially only `__init__.py` exists.

* **models/**
  Contains ORM model classes, typically one file per database table/entity.

* **schemas/**
  Contains Pydantic schemas for request/response validation and serialization. One file per schema/domain.

* **database.py**
  Contains database connection and session setup, used throughout the app.

* **alembic/** & **alembic.ini**
  Alembic migration environment and version scripts for managing database migrations.

* **core/**
  Core business logic, configuration, and utilities.

  * **config.py:** Settings (typically Pydantic-based, loaded from `.env`).
  * **exceptions.py:** Custom exception classes and error handlers.
  * **security.py:** Authentication and security logic.
  * **utils.py:** Miscellaneous helpers and utilities.

* **jobs/**
  For cron jobs, scheduled/background tasks. Place scripts or task modules here.

* **middleware/**
  Contains custom middleware for the application.

* **tests/**
  For all unit and integration tests.

* **README.md**
  Project overview, setup, usage instructions.

* **.env.example**
  Template for required environment variables.

* **Dockerfile** and **docker-compose.yml**
  For containerizing the app and defining services for local development or deployment.

---

## 4. **General Guidelines**

* **Add new features/entities** by creating new files in `models/`, `crud/`, `schemas/`, and `api/routers/` as needed.
* **Each folder only contains files for its specific concern**—avoid mixing unrelated logic.
* **Dependencies** are managed centrally in `api/deps.py`.
* **Business logic and security** live in the `core/` folder.
* **Cron/scheduled tasks** should go into `jobs/`.
* **Migrations** must use Alembic; keep the folder at project root.
* **Configuration** is loaded from `.env` via `core/config.py`.

---

## 5. **What the AI Coding Agent Should Do**

* Respect and extend this structure when adding features, models, endpoints, or background tasks.
* When generating new code (e.g., for a new entity), create or update the appropriate files in `models/`, `schemas/`, `crud/`, and `api/routers/`.
* Keep logic modular—do not place database access or business logic inside router functions.
* Always use dependency injection for DB sessions and other shared resources via `api/deps.py`.
* For new scheduled/background tasks, add files/modules to `jobs/`.
* For middleware, add new modules to `middleware/` and register them in `main.py`.
* Update `.env.example` and `README.md` if new configuration options are required.

---

**By following this structure, the project remains modular, clear, and easy to maintain or extend—by both humans and AI agents.**
