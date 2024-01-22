FROM python:3.11

ENV DEBUG=0

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache -r /tmp/requirements.txt
WORKDIR /tests/

RUN python -m spacy download en_core_web_md

COPY . .

RUN pytest -vv tests.py