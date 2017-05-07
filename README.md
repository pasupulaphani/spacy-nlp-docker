# spacy-nlp

SpaCy-1.7 python3

- Installs English tagger, parser and NER
- Installs English GloVe vectors

## Getting started

- Build locally

```
docker build -t spacy-nlp:en .
```

- (OR) Get latest from hub.docker.com

```
docker pull pasupulaphani/spacy-nlp:en
```

## Run tests

```
sh test.sh
```

### Get shell

```
docker run -it spacy-nlp /bin/bash
```

-------------------------------------

# spacy-nlp-zeromq

SpaCy with zeromq bindings

## Getting started

- Build locally

```
docker build -f Dockerfile.zeromq -t spacy-nlp-zeromq:en .
```
- (OR) Get latest from hub.docker.com

```
docker pull pasupulaphani/spacy-nlp-zeromq:en
```


### Start server

```
docker run --publish 4242:4242 -it spacy-nlp-zeromq:en
```
- (OR) Start manually

```
docker run -v ${PWD}:/usr/zeromq --publish 4242:4242 --entrypoint=/bin/bash  -it spacy-nlp-zeromq:en
python3 /usr/zeromq/zeromq/server.py
```


### API

##### parse
```
$ zerorpc  tcp://0.0.0.0:4242 parse "hotel new york"

u'[{"tag": "NN", "text": "hotel new york"}]'
```

##### entities
```
$ zerorpc  tcp://0.0.0.0:4242 entities "hotels in london"

u'[{"end": 6, "start": 0, "text": "hotels", "type": ""}, {"end": 16, "start": 10, "text": "london", "type": ""}]'
```


##### nounChunks
```
$ zerorpc  tcp://0.0.0.0:4242 nounChunks "hotels in london"

u'[{"text": "hotels"}, {"text": "london"}]'
```


# Troubleshoot


***Check if port is open***

```
if ! nc -z 0.0.0.0 4242 2>&1 >/dev/null; then echo "NOT AVAILABLE"; fi
```
