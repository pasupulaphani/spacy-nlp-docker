FROM pasupulaphani/spacy-nlp-docker:latest

MAINTAINER Phaninder <pasupulaphani@gmail.com>

ENV BASE_DIR /usr/zerorpc
ENV PORT     4242

RUN mkdir -p $BASE_DIR
VOLUME $BASE_DIR

WORKDIR $BASE_DIR
ADD . $BASE_DIR

########################################
# ZeroMQ
########################################
RUN apt-get install -y libzmq-dev

####################

# Install pyzmq: Python bindings for ZeroMQ
RUN apt-get install -y python-setuptools
RUN pip3 install -r $BASE_DIR/zeromq/requirements.txt

EXPOSE $PORT

ENTRYPOINT ["python3", "/usr/zerorpc/zeromq/server.py"]
