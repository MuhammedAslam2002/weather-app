# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application's port
EXPOSE 5000

# Define the environment variable for the API key
ENV OPENWEATHER_API_KEY=09650954118fd9fb482c4ef9aa18b723

# Run the application
CMD ["python", "app.py"]

