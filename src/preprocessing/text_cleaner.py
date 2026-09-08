import re
import spacy
nlp=spacy.load("en_core_web_sm")

def clean_text(text):

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    # Remove leading and trailing spaces
    text = text.strip()

    return text

def process_text(text):
    doc=nlp(text)
    return doc