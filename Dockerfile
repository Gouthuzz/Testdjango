# Use a lightweight Python 3.9 base image
FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy project code
COPY . .

# Environment variable (optional, useful for production)
ENV PYTHONUNBUFFERED 1

# Expose port for Django app
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
