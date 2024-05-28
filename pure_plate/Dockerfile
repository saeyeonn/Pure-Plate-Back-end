FROM python:3.9.6

WORKDIR /pure_plate

COPY . /pure_plate/.

#Dependencies setting
RUN pip install --no-cache-dir -r requirements.txt
# RUN apt-get update && apt-get install -y nginx

ENV DJANGO_SETTINGS_MODULE=pure_plate.settings
ENV PYTHONUNBUFFERED 1

# COPY nginx.conf /etc/nginx/sites-available/default
# RUN rm -f /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled
# RUN python manage.py collectstatic --noinput

CMD gunicorn --bind 0.0.0.0:8000 pure_/pure_plate/wsgi:application

EXPOSE 80