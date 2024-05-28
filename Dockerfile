FROM python:3.9.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
# 필요 패키지 복사 및 설치
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run on container start
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pureplate-backend.wsgi:application"]