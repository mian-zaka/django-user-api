
# django-user-api
REST API for user CRUD built with Django and Django REST Framework. Pagination, Swagger/ReDoc docs, CORS support.
## How to run the project (after cloning)

### 1. Clone the repository

```bash
git clone https://github.com/mian-zaka/django-user-api
cd django-user-api
```

### 2. Create a virtual environment (recommended)

**Windows (Command Prompt):**

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations (create database tables)

```bash
python manage.py migrate
```

### 5. (Optional) Create a superuser (for Django admin)

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

- **Swagger UI:** (http://127.0.0.1:8000/swagger/)
- **ReDoc:** (http://127.0.0.1:8000/redoc/)

---

## API endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/list-users/` | List users |
| `GET` | `/api/user/<id>/` | Get a single user by ID |
| `POST` | `/api/createUser` | Create a new user |
| `PUT` / `PATCH` | `/api/userUpdate/<id>/` | Update a user |
| `DELETE` | `/api/userDelete/<id>/` | Delete a user |

**User payload (create/update):** `first_name`, `last_name`, `email` (required; email must be unique).

---
