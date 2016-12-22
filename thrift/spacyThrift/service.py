from spacyThrift import SpacyThrift
from spacyThrift.ttypes import Token

from spacy.en import English

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import logging

class Handler:
    def __init__(self, nlp):
        self.nlp = nlp

    def tag(self, sentence):
        document = nlp(sentence, parse=False, entity=False)
        return [Token(element.orth_, element.tag_, element.lemma_)
                for element in document]

if __name__ == '__main__':
    logging.basicConfig()
    logger = logging.getLogger()

    logger.info("Loading ...")
    nlp = English(parser=False, tagger=True, entity=False)

    handler = Handler(nlp)
    processor = SpacyThrift.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    logger.info("Serving ...")
    server.serve()

