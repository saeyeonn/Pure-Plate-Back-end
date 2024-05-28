FROM python:3.9.6

# Set work directory
WORKDIR /pure_plate

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt /pure_plate/

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . /pure_plate/

# Environment variables
ENV DJANGO_SETTINGS_MODULE=pure_plate.settings
ENV PYTHONUNBUFFERED 1

# Uncomment the lines below if you are using nginx
# COPY nginx.conf /etc/nginx/sites-available/default
# RUN rm -f /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled
# RUN python manage.py collectstatic --noinput

# Command to run the application
CMD gunicorn --bind 0.0.0.0:8000 pure_plate.wsgi:application

# Expose the port the app runs on
EXPOSE 8000

# FROM python:3.9.6

# WORKDIR /pure_plate

# COPY . /pure_plate/.

# COPY requirements.txt /pure_plate/

# #Dependencies setting
# RUN pip install --no-cache-dir -r requirements.txt
# # RUN apt-get update && apt-get install -y nginx

# ENV DJANGO_SETTINGS_MODULE=pure_plate.settings
# ENV PYTHONUNBUFFERED 1

# # COPY nginx.conf /etc/nginx/sites-available/default
# # RUN rm -f /etc/nginx/sites-enabled/default && ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled
# # RUN python manage.py collectstatic --noinput

# CMD gunicorn --bind 0.0.0.0:8000 pure_/pure_plate/wsgi:application

# EXPOSE 80