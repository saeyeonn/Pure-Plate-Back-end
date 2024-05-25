FROM python:3.9.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /code/

# Expose the port the app runs on
EXPOSE 8000

# Command to run on container start
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]