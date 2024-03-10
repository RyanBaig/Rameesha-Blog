#!/bin/bash

# Build the project
echo "Building project..."
python3.9 -m pip install -r requirements.txt

echo "Making Migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput
