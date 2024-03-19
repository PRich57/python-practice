# Use Python runtime as parent image
FROM python:3.8-slim

# Set working directory
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run project.py when the container launches
CMD ["python", "./project.py"]