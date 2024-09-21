# Use the official Python image with version 3.9
FROM python:3.10-slim

# Install build tools
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
# COPY requirements.txt requirements.txt
COPY . .
RUN pip install -r requirements.txt

# Copy all files from the current directory to the working directory in the container
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app/ui.py", "--server.port=8501", "--server.address=0.0.0.0"]