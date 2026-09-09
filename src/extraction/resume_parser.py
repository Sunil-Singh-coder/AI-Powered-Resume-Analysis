# Clean Text
#      ↓
# spaCy
#      ↓
# Tokens
# POS
# Entities
# Sentences

import re   # regular expression 
from src.preprocessing.text_cleaner import clean_text,process_text
from src.skills.skill_extractor import extract_skills
import fitz
# For pdf extraction we use fitz

def extract_text_from_pdf(pdf_path):
   document=fitz.open(pdf_path)
   text=""
   for page in document:
       text += page.get_text()
   document.close()

   return text

# testing  purpose 
# pdf_path="data/resumes/Resume_ML.pdf"
# 1. # extract pdf  
# resume_text= extract_text_pdf(pdf_path)

# 2.# clean the resume text 
# cleaned_text=clean_text(resume_text)

# # 3.process the text
# doc =process_text(cleaned_text)
# # for token in doc:
# #     print(token.text, "->", token.pos_)

# # 4 Skills extration 
# resume_skills=extract_skills(cleaned_text)
# print("Detected Skills")
# print(resume_skills)


