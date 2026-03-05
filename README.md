# Subscription Based Content API

A Django REST Framework API implementing a subscription-based content access system. Users can register, upgrade to premium, access protected content, and generate usage analytics.

## Features

### User Roles

* Free users
* Premium users
* Subscription expiry tracking

### Premium Content Protection

* Only users with active premium subscription can access protected endpoints
* Automatic subscription expiration validation

### Subscription Upgrade

* Endpoint to upgrade Free → Premium
* Premium duration: 30 days
* If upgraded again while active, 30 days are added

### Activity Logging

Logs each premium access with:

* User
* Endpoint
* HTTP Method
* IP Address
* Timestamp

### Admin Analytics

Admin can:

* View access logs
* Generate monthly CSV reports

## Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

## Project Structure

```
subscriptions/
│
├── api/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── utils.py
│   └── urls.py
│
├── subscriptions/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── README.md
```

## API Endpoints

### Register

POST /api/register/

Creates a new user.

Example:

```
{
  "email": "user@example.com",
  "password": "password123"
}
```

### Premium Content

GET /api/premium-content/

Requires authentication and premium subscription.

Response:

```
{
  "detail": "Welcome to the premium content!"
}
```

### Upgrade Subscription

POST /api/upgrade-subscription/

Upgrades user to premium.

Response:

```
{
  "detail": "Subscription upgraded successfully",
  "subscription_expiry": "2026-04-02T20:42:46Z"
}
```

### Access Logs (Admin)

GET /api/access-logs/

Returns premium access logs.

### Monthly CSV Report

GET /api/monthly-report/?year=2026&month=3

Downloads CSV usage report.

## Running Locally

### Clone repo

```
git clone https://github.com/yourusername/subscription-based-content-api.git
cd subscription-based-content-api
```

### Create virtual environment

```
python -m venv venv
```

Activate:

Mac/Linux

```
source venv/bin/activate
```

Windows

```
venv\\Scripts\\activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run migrations

```
python manage.py migrate
```

### Create admin

```
python manage.py createsuperuser
```

### Start server

```
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

## Testing

You can test using:

* Postman
* curl
* REST Client

Authentication header:

```
Authorization: Bearer <token>
```

## Optional Features Implemented

* Subscription expiration logic
* Monthly CSV analytics reports
* Admin access log endpoint
* Premium activity tracking

## Future Improvements

* Stripe payment integration
* PostgreSQL database
* Redis caching
* Rate limiting
* Dashboard analytics

## Author

Prince Rai


