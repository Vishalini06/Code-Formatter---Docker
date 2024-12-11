# Use an official Python runtime as the base image
FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /django

# Copy the requirements.txt first to leverage Docker cache for dependencies
COPY requirements.txt requirements.txt 

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application files into the container
COPY . .


CMD python manage.py runserver 0.0.0.0:8000
# Expose port 8000 to access the app externally


# Define environment variables (Optional: Add sensitive data or debugging)



