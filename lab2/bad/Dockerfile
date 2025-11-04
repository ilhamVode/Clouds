FROM python:latest

RUN apt-get update
RUN pip install requests
RUN apt-get install -y nginx

COPY app/ /app

CMD ["python", "/app/main.py"]
