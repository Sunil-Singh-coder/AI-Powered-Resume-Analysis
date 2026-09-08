import pymupdf
import fitz
import re     # 

# how to convert text into Name identity form
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Python is a programming language. ")
for token in doc:
    print(token.text, token.pos_)


# For pdf extraction we use fitz
# document=fitz.open("data/SUNIL_RESUME.pdf")
# text=""
# for page in document:
#      text += page.get_text()
# print(text) 
# document.close()