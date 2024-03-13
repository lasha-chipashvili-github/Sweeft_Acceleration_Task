FROM python:3.10-slim

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
EXPOSE 8000

COPY . .
