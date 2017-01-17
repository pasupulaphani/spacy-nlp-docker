import zerorpc
import os
import sys
import json
import spacy
import spacy.util

sys.path.append(os.path.join(os.path.dirname(__file__), '../spacyParser'))
from parse import Parse
from entities import Entities
from noun_chunks import NounChunks

port = os.environ.get('PORT')

print("Loading model: 'en'")
enNlpModel = spacy.load('en')
print("Loaded model: 'en'")

class SpacyNlpRPC(object):
    def parse(self, text):
        p = Parse(enNlpModel, text)
        return json.dumps(p.to_json(), sort_keys=True)
    def entities(self, text):
        e = Entities(enNlpModel, text)
        return json.dumps(e.to_json(), sort_keys=True)
    def nounChunks(self, text):
        ncs = NounChunks(enNlpModel, text)
        return json.dumps(ncs.to_json(), sort_keys=True)

s = zerorpc.Server(SpacyNlpRPC())
s.bind("tcp://0.0.0.0:" + port)
s.run()
