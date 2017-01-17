import os
import sys
import spacy

sys.path.append(os.path.join(os.path.dirname(__file__), '../spacyParser'))

from noun_chunks import NounChunks

lang = os.environ.get('LANG')
nlp = spacy.load(lang)

input = u'hotel new york'
expected = ['hotel', 'new york']

ncs = NounChunks(nlp, input)
actual = ncs.to_list()
print('expected: ')
print(expected)
print('actual: ')
print(actual)


if expected == actual:
    print('Noun chunks successful')
else:
    raise Exception('Noun chunks not same')
