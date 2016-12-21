import spacy

nlp = spacy.load('en')

def get(text):

    result = []
    doc = nlp(text)

    for np in doc.noun_chunks:
        result.append(np.text)

    return result
