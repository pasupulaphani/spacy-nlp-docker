FROM pasupulaphani/spacy-nlp:en

MAINTAINER Phaninder <pasupulaphani@gmail.com>

ENV BASE_DIR          /usr/zeromq
ENV PORT              4242

RUN mkdir -p $BASE_DIR
VOLUME $BASE_DIR

WORKDIR $BASE_DIR
ADD . $BASE_DIR

########################################
# ZeroMQ
########################################
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git build-essential libtool autoconf automake pkg-config unzip libkrb5-dev
RUN cd /tmp && git clone git://github.com/jedisct1/libsodium.git && cd libsodium && git checkout e2a30a && ./autogen.sh && ./configure && make check && make install && ldconfig
RUN cd /tmp && git clone --depth 1 git://github.com/zeromq/libzmq.git && cd libzmq && ./autogen.sh && ./configure && make
# RUN cd /tmp/libzmq && make check
RUN cd /tmp/libzmq && make install && ldconfig
RUN rm /tmp/* -rf

####################

# Install pyzmq: Python bindings for ZeroMQ
RUN apt-get install -y python3-setuptools
RUN pip3 install -r $BASE_DIR/zeromq/requirements.txt

EXPOSE $PORT

ENTRYPOINT ["python3", "/usr/zeromq/zeromq/server.py"]
