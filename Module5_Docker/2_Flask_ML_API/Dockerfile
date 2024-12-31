FROM python:3.8-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

RUN pip install flask scikit-learn numpy flask-sqlalchemy psycopg2-binary

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]

