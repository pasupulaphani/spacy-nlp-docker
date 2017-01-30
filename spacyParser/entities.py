class Entities(object):
    def __init__(self, nlp, text):
        self.doc = nlp(text)

        for np in list(self.doc.noun_chunks):
            np.merge(np.root.tag_, np.root.lemma_, np.root.ent_type_)

    def to_json(self):
        return [{'text': ent.text, 'start': ent.start_char, 'end': ent.end_char, 'type': ent.label_}
                for ent in self.doc.ents]
