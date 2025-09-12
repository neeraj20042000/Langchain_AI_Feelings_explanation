# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port (if your app runs on a specific port, e.g., 8000)
EXPOSE 8000

# Set entrypoint (update if your main file or command is different)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
