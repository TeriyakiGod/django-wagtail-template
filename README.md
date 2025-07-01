# Django Wagtail Template

A modern Django CMS template built with Wagtail, featuring Docker containerization and automated deployment.

## Features

- **Wagtail CMS** - Powerful content management system
- **PostgreSQL** - Production-ready database
- **Docker** - Containerized development and deployment
- **Pre-commit hooks** - Code quality enforcement with Black formatter
- **GitHub Actions** - Automated CI/CD pipeline

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd django-wagtail-template
   ```

2. **Run with Docker**
   ```bash
   docker-compose up --build
   ```

3. **Run migrations and collect static files**
   ```bash
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py collectstatic --noinput
   ```

4. **Create a superuser**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Access the application**
   - Website: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Local Development (without Docker)

1. **Start the database**
   ```bash
   docker-compose up db
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations and collect static files**
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

4. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## Development

- **Django Admin**: http://localhost:8000/django-admin/
- **Wagtail Admin**: http://localhost:8000/admin/
- **Search**: http://localhost:8000/search/

## Environment Variables

Create a `.env` file with:
```env
DJANGO_SECRET_KEY=your-secret-key
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

## Deployment

The project includes automated deployment via GitHub Actions to CapRover. Configure the following secrets in your repository:

- `CAPROVER_SERVER`
- `APP_NAME`
- `APP_TOKEN`

## Tech Stack

- Django 5.2.3
- Wagtail 7.0.1
- PostgreSQL
- Gunicorn
- Docker & Docker Compose
