@echo
cd api_project
python manage.py makemigrations
python manage.py migrate
python manage.py runserver