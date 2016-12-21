# spacy-nlp-docker

SpaCy python3

- Installs English tagger, parser and NER
- Installs English GloVe vectors

## Getting started

- Build locally

```
docker build -t spacy-nlp .
```

- (OR) Get latest from hub.docker.com

```
docker pull pasupulaphani/spacy-nlp-docker:en
```

## Run tests

```
sh test.sh
```

### Get shell

```
docker run -it spacy-nlp /bin/bash
```
