import streamlit as st
import spacy
from spacy import displacy

# Load the spaCy model
nlp = spacy.load("./model-last/")

# Function to extract entities from text
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities, doc

# Streamlit app
def main():
    st.title("Legal NER")

    # Text input
    text = st.text_area("Enter some text:")

    # Button to extract entities
    if st.button("Extract Entities"):
        if text.strip() != "":
            entities, doc = extract_entities(text)
            if entities:
                html = displacy.render(doc, style="ent", page=False)
                st.write(html, unsafe_allow_html=True)
            else:
                st.write("No entities found.")
        else:
            st.write("Please enter some text.")

if __name__ == "__main__":
    main()
