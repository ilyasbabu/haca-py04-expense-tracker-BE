# ✦ Expense Tracker — Backend

A Django REST API backend for the Expense Tracker app, featuring JWT authentication, Google OAuth, and Gemini AI integration.

🔗 **Frontend**: [haca-py04-expense-tracker.netlify.app](https://haca-py04-expense-tracker.netlify.app/)  
📦 **Repo**: [github.com/ilyasbabu/haca-py04-expense-tracker-BE](https://github.com/ilyasbabu/haca-py04-expense-tracker-BE)

---

## Tech Stack

- **Django 6** — web framework
- **Django REST Framework** — API layer
- **SimpleJWT** — JWT-based authentication
- **Google Auth** — OAuth 2.0 login
- **Google Gemini (`google-genai`)** — AI integration
- **django-cors-headers** — cross-origin request handling
- **python-dotenv** — environment variable management

## Project Structure

```
haca-py04-expense-tracker-BE/
├── expense_tracker_backend/   # Django project settings & URLs
├── expenses/                  # Expense models, views, serializers
├── users/                     # User auth, registration, Google OAuth
├── manage.py
└── requirements.txt
```

## Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/ilyasbabu/haca-py04-expense-tracker-BE.git
cd haca-py04-expense-tracker-BE
```

**2. Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:
```env
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

GOOGLE_CLIENT_ID=your_google_oauth_client_id
GOOGLE_CLIENT_SECRET=your_google_oauth_client_secret
GEMINI_API_KEY=your_gemini_api_key
```

**5. Run migrations**
```bash
python manage.py migrate
```

**6. Start the development server**
```bash
python manage.py runserver
```

API will be available at `http://localhost:8000/`

## Authentication

- **JWT** — obtain tokens via `/api/token/`, refresh via `/api/token/refresh/`
- **Google OAuth** — sign in with Google via the `users` app endpoints

## Key Dependencies

| Package | Purpose |
|---|---|
| `djangorestframework` | REST API framework |
| `djangorestframework-simplejwt` | JWT auth tokens |
| `google-auth` | Google OAuth 2.0 |
| `google-genai` | Gemini AI integration |
| `django-cors-headers` | CORS for frontend connection |
| `python-dotenv` | `.env` file support |

---

Built with care from HACA