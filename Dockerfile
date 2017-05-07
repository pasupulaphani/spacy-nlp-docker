FROM python:3.5-slim

MAINTAINER Phaninder <pasupulaphani@gmail.com>

ENV LANG             en
ENV SPACY_VERSION    1.7

RUN mkdir -p /usr/spacy
COPY . /usr/spacy/

RUN apt-get update
RUN apt-get install -y build-essential python-dev git

RUN pip3 install --upgrade pip setuptools

########################################
# spaCy
########################################
RUN pip3 install spacy==${SPACY_VERSION}
RUN python3 -m spacy.${LANG}.download all

# Check whether the model was successfully installed
RUN python3 /usr/spacy/test/load_lang.py
###################

WORKDIR /usr/spacy

CMD ["python3"]
