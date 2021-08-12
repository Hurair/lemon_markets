FROM python:3.8

WORKDIR /app

RUN pip install pipenv
COPY Pipfile* /app/
# install service dependencies from the lock file
RUN pipenv install --system --deploy

COPY service/ service/
COPY tests/ test/


ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app


CMD ["python", "service/app.py"]
