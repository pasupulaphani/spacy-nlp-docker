namespace py spacyThrift

struct Token {
  1: string word,
  2: string tag,
  3: string lemma
}

service SpacyThrift {
  list<Token> tag(1: string sentence)
}
