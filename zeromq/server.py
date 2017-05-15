import zerorpc
import os
import logging, sys
import json
import spacy
import spacy.util

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
sys.path.append(os.path.join(os.path.dirname(__file__), '../spacyParser'))

from parse import Parse
from entities import Entities
from noun_chunks import NounChunks

port = os.environ.get('PORT')

logging.info("Loading model: 'en'")
enNlpModel = spacy.load('en')
logging.info("Loaded model: 'en'")

def decodeReqText(data):
    if isinstance(data, (bytes, bytearray)):
        return data.decode("utf-8")
    else:
        return data


class SpacyNlpRPC(object):
    def parse(self, data):
        text = decodeReqText(data)
        print('parse: text - ' + text)
        p = Parse(enNlpModel, text)
        res = json.dumps(p.to_json(), sort_keys=True)
        logging.debug('parse: result - ' + res)
        return res
    def entities(self, data):
        text = decodeReqText(data)
        logging.debug('entities: text - ' + text)
        e = Entities(enNlpModel, text)
        res = json.dumps(e.to_json(), sort_keys=True)
        logging.debug('entities: result - ' + res)
        return res
    def nounChunks(self, data):
        text = decodeReqText(data)
        logging.debug('nounChunks: text - ' + text)
        ncs = NounChunks(enNlpModel, text)
        res = json.dumps(ncs.to_json(), sort_keys=True)
        logging.debug('nounChunks: result - ' + res)
        return res

s = zerorpc.Server(SpacyNlpRPC())

host = "tcp://0.0.0.0:" + port
logging.info("Listening on: " + host)
s.bind(host)
s.run()
