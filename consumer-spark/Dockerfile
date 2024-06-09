# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /consumer-spark

# Copy the current directory contents into the container at /app
COPY . /consumer-spark

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y default-jre && \
    apt-get install -y ant && \
    apt-get clean;
RUN pip install -r requirements.txt



# Run writetospark.py when the container launches
CMD ["python", "machinelearning.py"]

