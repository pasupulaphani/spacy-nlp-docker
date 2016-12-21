import spacy

nlp = spacy.load('en')

def noun_chunks(text):
    result = []
    doc = nlp(text)
    for np in doc.noun_chunks:
        result.append(np.text)
    return result


input = u'hotel new york'
expected = ['hotel', 'new york']

actual = noun_chunks(input)
print('expected: ')
print(expected)
print('actual: ')
print(actual)

if cmp(expected, actual) == 0:
    print('Noun chunks successful')
else:
    raise Error('Noun chunks not same')
