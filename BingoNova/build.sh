#!/usr/bin/env bash
# Script de build para Render
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# Crea el superusuario automáticamente si no existe (usando variables de entorno).
# Si ya existe, este comando falla silenciosamente gracias al "|| true".
python manage.py createsuperuser --no-input || true
