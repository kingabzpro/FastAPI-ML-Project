import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp ("Apple buys U.K startup for $1 billion")

for ent in doc.ents:
    print(ent.text,ent.label_)