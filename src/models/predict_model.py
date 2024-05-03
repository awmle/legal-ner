# Using spacy.load().
import spacy
nlp = spacy.load("en_legal_ner_sm")
text = "Section 319 Cr.P.C. contemplates a situation where the evidence adduced by the prosecution for Respondent No.3-G. Sambiah on 20th June 1984"
doc = nlp(text)

# Print indentified entites
for ent in doc.ents:
     print(ent,ent.label_)

##OUTPUT     
#Section 319 PROVISION
#Cr.P.C. STATUTE
#G. Sambiah RESPONDENT
#20th June 1984 DATE
