# Subscription Based Content API

A Django REST API implementing a subscription-based access control system.

## Features

- Free and Premium user roles
- Premium content protection
- Subscription upgrade endpoint
- Premium access activity logging
- Monthly usage report (CSV)
- Admin analytics endpoint

## Run Locally

1. Clone repo
2. Install dependencies

pip install -r requirements.txt

3. Run migrations

python manage.py migrate

4. Create admin user

python manage.py createsuperuser

5. Start server

python manage.py runserver