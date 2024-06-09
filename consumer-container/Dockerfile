# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /consumer-container

# Copy the current directory contents into the container at /app
COPY . /consumer-container

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir confluent_kafka pymongo requests 


# Run consumer.py when the container launches
CMD ["python", "consumer.py"]


