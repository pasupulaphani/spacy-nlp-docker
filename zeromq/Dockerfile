FROM spacy-nlp:latest

MAINTAINER Phaninder <pasupulaphani@gmail.com>

ENV BASE_DIR /usr/zeromq
ENV PORT     4242

RUN mkdir -p $BASE_DIR
VOLUME $BASE_DIR

WORKDIR $BASE_DIR
ADD zeromq $BASE_DIR

########################################
# ZeroMQ
########################################
RUN apt-get install -y libzmq-dev

####################

# Install pyzmq: Python bindings for ZeroMQ
RUN apt-get install -y python-setuptools
RUN pip3 install -r $BASE_DIR/requirements.txt

EXPOSE $PORT

ENTRYPOINT ["python3", "/usr/zeromq/server.py"]
