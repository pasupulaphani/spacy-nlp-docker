# spacy-nlp-zeromq-docker

SpaCy zeromq

## Getting started

- Build locally

```
docker build -t spacy-nlp-zeromq .
```


### Get shell

```
docker run -v ${PWD}:/usr/zeromq --publish 4242:4242 -it spacy-nlp-zeromq /bin/bash
```
