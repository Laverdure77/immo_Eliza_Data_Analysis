FROM python:3.10.1
RUN mkdir /app
WORKDIR /app 
COPY requirements.txt  .
RUN pip install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "/app/eliza_estimate.py", "--host=0.0.0.0"]