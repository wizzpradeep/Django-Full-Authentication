# Full Authentication Django App

This is a **full authentication Django app** built with **Python** and **Django** on the backend and **HTML + Tailwind CSS** on the frontend. The app provides robust authentication features, including:

- User registration with real email verification.
- Login and logout functionality.
- Password reset (Forgot Password).
- Password change for logged-in users.

## Features
- Secure and reliable user authentication.
- Responsive and modern frontend design using Tailwind CSS.
- Real email verification for account activation.
- Easily customizable for other projects.

---

## Installation and Setup Guide

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/wizzpradeep/Django-Full-Auth
cd Django-Full-Authentication
```
### 2. Create a Virtual Environment
```bash
python -m venv .env
source .env/bin/activate # On Linux/Mac
.env\Scripts\activate    # On Windows
```
### 3. Install Dependencies
```bash
pip install -r req.txt
```
### 4. Set Up Environment Variables
```bash
settings.py
SECRET_KEY=your-django-secret-key
"Run this command for secret key"
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=yourpassword
```
### 5. Apply Migrations and run the Server
```bash
python manage.py migrate
python manage.py runserver
```
