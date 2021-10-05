release: python manage.py makemigrations && python manage.py migrate
web: gunicorn mysite.wsgi
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate