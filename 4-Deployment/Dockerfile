FROM python:3.10.1
RUN mkdir /app
COPY requirements.txt /app
COPY . /app
WORKDIR /app 
RUN ls -la /app/*
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python3", "eliza_estimate.py", "--host=0.0.0.0"]


# run the image using: docker run -t -i -p 5000:5000 <name of image>