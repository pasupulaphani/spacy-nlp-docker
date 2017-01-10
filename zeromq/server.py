import zerorpc
import os
import json
import spacy
import spacy.util

from parse import Parse, Entities

port = os.environ.get('PORT')
enNlpModel = spacy.load('en')
print("Loaded model: 'en'")

class SpacyNlpRPC(object):
    def parse(self, text):
        parse = Parse(enNlpModel, text)
        return json.dumps(parse.to_json(), sort_keys=True, indent=2)
    def entities(self, text):
        entities = Entities(enNlpModel, text)
        return json.dumps(entities.to_json(), sort_keys=True, indent=2)

s = zerorpc.Server(SpacyNlpRPC())
s.bind("tcp://0.0.0.0:" + port)
s.run()
