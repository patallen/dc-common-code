FROM python:3

RUN mkdir code
WORKDIR code

COPY ./application ./application

RUN pip install -r application/requirements.txt

RUN ls -la