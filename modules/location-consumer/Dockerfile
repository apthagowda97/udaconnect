FROM python:3.7-slim

WORKDIR .

RUN apt-get gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .
CMD ["python","app/main.py"]
