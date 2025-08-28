# ALX Travel App 0x03

This is a Django travel booking app.

## Features

- Booking creation
- Background tasks with Celery & RabbitMQ
- Listings management

## Setup

1. Create a virtual environment
2. Install dependencies: pip install -r requirements.txt
3. Start RabbitMQ (or Docker RabbitMQ)
4. Run Celery worker: celery -A alx_travel_app worker --loglevel=info
5. Run Django server: python manage.py runserver

