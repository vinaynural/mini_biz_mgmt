#!/bin/bash
set -o errexit

echo "Running makemigrations..."
python manage.py makemigrations core customers products orders

echo "Running migrate..."
python manage.py migrate

echo "Creating superuser..."
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin123')"

echo "Starting Server..."
gunicorn config.wsgi:application
