FROM python:3.8.2

RUN apt update && apt upgrade -y
RUN apt-get install build-essential libc6-dbg python3-dev -y

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /app
COPY ./requirements-test.txt /app

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt

COPY ./* /app/
