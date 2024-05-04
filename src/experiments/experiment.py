

# Create training config
# python -m spacy init fill-config ./src/experiments/base_config.cfg ./src/experiments/config.cfg

import spacy

trained_nlp = spacy.load("./models/model-best")
text = "In this reference under Section 66 (1) of the Indian Income-tax Act, 1922, at the instance of the assessee Messrs. Dayabhai & Co. of Barwani, the question posed for our answer is: \n \"Whether on the facts and in the circumstances of this case, the assessee is entitled to registration under Section 26-A of the Indian Income-tax Act for the assessment year 1956-57?\" \n 2."
doc = trained_nlp(text)

for ent in doc.ents:
    print (ent.text, ent.label_)