# Week 4 — Django Web Framework Setup 🚀

This folder contains the initial Django project setup for **Spendora**, started during Week 4 of the eMobilis Fullstack Development course.

## Project Structure

```
week_4/
├── manage.py              # Django management script
├── spendora/              # Project root / configuration
│   ├── __init__.py
│   ├── asgi.py            # ASGI config for async deployment
│   ├── settings.py        # Project settings & installed apps
│   ├── urls.py            # Global URL routing
│   └── wsgi.py            # WSGI config for web servers
├── spendora_app/          # Main application module
│   ├── admin.py           # Admin panel registration
│   ├── apps.py            # App configuration (SpendoraAppConfig)
│   ├── models.py          # Database models (ORM)
│   ├── tests.py           # Unit tests
│   ├── views.py           # Request handlers / views
│   └── migrations/        # Database schema migrations
└── README.md
```

## Getting Started

### 1. Set Up Virtual Environment

From within the `week_4/` folder:

```bash
# Create virtual environment (if not already created)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate       # macOS / Linux
# or: venv\Scripts\activate    # Windows
```

### 2. Install Django

```bash
pip install django
```

### 3. Run Migrations & Start Development Server

```bash
# Run database migrations
python manage.py migrate

# Start the dev server
python manage.py runserver
```

Open your browser and navigate to: **`http://127.0.0.1:8000/`** to view the default Django welcome page.

## Notes

- `db.sqlite3` is ignored by Git to avoid database merge conflicts and local data leaks.
- Virtual environments (`venv/`) and Python bytecode (`__pycache__/`) are ignored via `.gitignore`.
- App `'spendora_app'` is registered in `spendora/settings.py` under `INSTALLED_APPS`.
