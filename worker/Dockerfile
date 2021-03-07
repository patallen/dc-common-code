FROM python:3

RUN mkdir code
WORKDIR code

COPY ./worker ./worker

RUN pip install -r worker/requirements.txt

RUN ls -la