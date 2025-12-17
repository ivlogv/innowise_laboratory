# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install uv package manager
RUN pip install --no-cache-dir uv

# Copy the current directory contents into the container at /app
COPY . .

# Install dependencies using uv
RUN uv pip install --system -r requirements.lock

# Make port 8000 available to the world outside this container
# Use 'docker pun -p 8000:8000 app:latest' to map the port correctly
EXPOSE 8000

# Run the uvicorn server when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]