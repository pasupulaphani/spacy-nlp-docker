class NounChunks(object):
    def __init__(self, nlp, text):
        self.doc = nlp(text)
        for np in list(self.doc.noun_chunks):
            np.merge(np.root.tag_, np.root.lemma_, np.root.ent_type_)

    def to_json(self):
        words = [{'text': nc.text} for nc in self.doc.noun_chunks]
        return words

    def to_list(self):
        words = [nc.text for nc in self.doc.noun_chunks]
        return words
