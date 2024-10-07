# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the entire Django project into the container
COPY . /app/

# Expose port 8000 for the Django app to be accessible
EXPOSE 8000

# Run Django's built-in development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
