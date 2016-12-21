import os

lang = os.environ.get('LANG')

spacy.load(lang)
print('Loaded ' + lang + ' OK')"
