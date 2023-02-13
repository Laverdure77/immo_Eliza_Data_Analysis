# Load Python image from docker Hub
FROM python:3.10.1

# Create a app directory in the docker image
RUN mkdir /app

# Set working directory /app as default
WORKDIR /app 

# Copy the requirements.txt (pipreqs) file containing all necessary
# libraries from deployment folder to docker image /app 
COPY requirements.txt /app

# Update pip 
RUN python -m pip install --upgrade pip

# Install requirements
RUN pip3 install -r requirements.txt

# Copy all files and folder from deployment to docker image /app
COPY . /app

# Should display app/ folder structure
RUN ls -la /app/*

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD ["python3", "eliza_estimate.py"]

# build the image using: docker build . -t <name of image>
# run the image using: docker run -t -i -p 5000:5000 <name of image>