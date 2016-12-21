import spacy
import os

lang = os.environ.get('LANG')

print('Loading parser: ' + lang)
spacy.load(lang)
