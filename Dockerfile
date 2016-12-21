FROM python:3.5-slim

MAINTAINER Phaninder <pasupulaphani@gmail.com>

ENV LANG en
ENV PORT 5000

RUN mkdir -p /usr/spacy
COPY . /usr/spacy/

RUN apt-get update
RUN apt-get install -y build-essential python-dev git

RUN pip3 install --upgrade pip setuptools

########################################
# spaCy
########################################
RUN pip3 install -r /usr/spacy/requirements.txt
RUN python3 -m spacy.${LANG}.download all

# Check whether the model was successfully installed
RUN python -c "import spacy; spacy.load('${LANG}'); print('OK')"
###################

EXPOSE ${PORT}
ENTRYPOINT cd /usr/spacy
