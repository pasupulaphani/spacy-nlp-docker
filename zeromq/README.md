# spacy-nlp-zeromq-docker

SpaCy zeromq

## Getting started

- Build locally

```
docker build -f Dockerfile.zeromq -t spacy-nlp-zeromq .
```


### Get shell

```
docker run -v ${PWD}:/usr/zeromq --publish 4242:4242 --entrypoint=/bin/bash  -it spacy-nlp-zeromq
```
