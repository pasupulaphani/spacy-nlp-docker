class Entities(object):
    def __init__(self, nlp, text):
        self.doc = nlp(text)

    def to_json(self):
        return [{'text': ent.text, 'start': ent.start_char, 'end': ent.end_char, 'type': ent.label_}
                for ent in self.doc.ents]
