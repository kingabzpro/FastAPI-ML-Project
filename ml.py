import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp ("COVID has trickled back into China. Beijing is responding with a tsunami of containment measures.")

for ent in doc.ents:
    print(ent.text,ent.label_)
