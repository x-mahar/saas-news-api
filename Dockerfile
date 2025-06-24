# Use an official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install OS dependencies (if needed)
RUN apt-get update && apt-get install -y build-essential

# Copy all project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
