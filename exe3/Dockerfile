FROM python:3.7-slim
WORKDIR /app
COPY ./app.py /app
RUN pip install flask
RUN pip install -U Flask-SQLAlchemy
CMD ["python", "./app.py"]
