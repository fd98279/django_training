# django_training

### Commands
workon django
pip install django
django-admin startproject first_project
cd first_project/
python manage.py run_server
python manage.py startapp first_app

migrations:
python manage.py makemigrations
python manage.py sqlmigrate first_app 0001
python manage.py migrate

python manage.py collectstatic
pip install djangorestframework==3.10

python manage.py shell
