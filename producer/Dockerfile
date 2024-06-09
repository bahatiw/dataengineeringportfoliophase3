# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /producer

# Copy the current directory contents into the container at /app
COPY . /producer

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir faker confluent_kafka 

# Run generatedata.py when the container launches
CMD ["python", "generatedata.py"]
