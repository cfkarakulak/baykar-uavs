#!/bin/bash
set -e

# run the app
cd /app

python3.8 manage.py makemigrations
python3.8 manage.py migrate
python3.8 manage.py loaddata sample
python3.8 manage.py runserver 0.0.0.0:8000
