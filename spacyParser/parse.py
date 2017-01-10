class Parse(object):
    def __init__(self, nlp, text):
        self.doc = nlp(text)
        spans = []
        for word in self.doc[:-1]:
            if word.is_punct:
                continue
            if not word.nbor(1).is_punct:
                continue
            start = word.i
            end = word.i + 1
            while end < len(self.doc) and self.doc[end].is_punct:
                end += 1
            span = self.doc[start : end]
            spans.append(
                (span.start_char, span.end_char, word.tag_, word.lemma_, word.ent_type_)
            )
        for span_props in spans:
            self.doc.merge(*span_props)

        for np in list(self.doc.noun_chunks):
            np.merge(np.root.tag_, np.root.lemma_, np.root.ent_type_)

    def to_json(self):
        words = [{'text': w.text, 'tag': w.tag_} for w in self.doc]
        return words
