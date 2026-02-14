# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Healthcare Triage Management System with a React frontend and Django REST API backend. Nurses create triage requests for patients; doctors view assigned requests. Anthropic API is integrated for AI-powered risk prediction.

## Architecture

**Two independent apps in one repo:**
- `frontend/` — React 19 SPA (Create React App)
- `Triage/` — Django 6 project with a single app (`login/`)

**Data flow:** React frontend → fetch with credentials → Django REST Framework API → SQLite

**Auth:** Django session-based authentication. User roles determined by Django groups (`Nurses`, `Doctors`). Views use `AllowAny` permission class but manually check group membership.

**Models (Triage/login/models.py):**
- `StaffProfile` — extends Django User (employee_id, department)
- `Patient` — patient demographics and medical history
- `TriageRequest` — links Patient, Nurse, Doctor with symptoms, vitals, predicted_risk, recommended_department

## Commands

### Frontend (from `frontend/`)
```bash
npm start          # Dev server on :3000
npm run build      # Production build
npm test           # Jest test runner
```

### Backend (from `Triage/`)
```bash
python manage.py runserver              # Dev server on :8000
python manage.py makemigrations login   # After model changes
python manage.py migrate                # Apply migrations
python manage.py createsuperuser        # Create admin user
```

No `requirements.txt` exists. Backend dependencies: `django`, `djangorestframework`, `django-cors-headers`, `python-dotenv`, `anthropic`.

## API Endpoints

All defined in `Triage/login/urls.py`:
- `POST /api/login/` — session login
- `POST /api/logout/` — logout
- `GET /api/user-role/` — returns `{role: "nurse"|"doctor"|"none"}`
- `GET /api/nurse-dashboard/` — triage requests for logged-in nurse
- `GET /api/doctor-dashboard/` — assigned requests for logged-in doctor

## Key Configuration

- **API base URL** is hardcoded in frontend pages (e.g., `http://192.168.18.207:8000`) — update when changing environments
- **CORS:** `CORS_ALLOW_ALL_ORIGINS = True` in `Triage/Triage/settings.py`
- **Anthropic API key** loaded from root `.env` file via `python-dotenv`
- **Database:** SQLite at `Triage/db.sqlite3`
- **CSRF trusted origins:** configured for `localhost:3000` and `192.168.18.207:3000`

## Frontend Structure

`frontend/src/App.js` defines three routes:
- `/` → `Login.js` (redirects based on role after auth)
- `/nurse` → `NurseDashboard.js`
- `/doctor` → `DoctorDashboard.js`

All API calls use `fetch` with `credentials: 'include'` for session cookies and pass CSRF tokens from cookies.
