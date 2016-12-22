import zerorpc
import os

port = os.environ.get('PORT')

import spacy

nlp = spacy.load('en')

def noun_chunks(text):
    result = []
    doc = nlp(text)
    for np in doc.noun_chunks:
        result.append(np.text)
    return result


class SpacyNlpRPC(object):
    def parse(self, text):
        return noun_chunks(text)

s = zerorpc.Server(SpacyNlpRPC())
s.bind("tcp://0.0.0.0:" + port)
s.run()
