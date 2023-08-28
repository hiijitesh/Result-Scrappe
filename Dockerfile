# Use the official Python base image
FROM python:3.8

# Set working directory within the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the app's files into the container
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 5000

# Set the entry point to start the Flask app
# CMD ["python", "app.py"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
