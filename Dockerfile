FROM python:3.10-alpine

COPY . /alembic
WORKDIR /alembic

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
