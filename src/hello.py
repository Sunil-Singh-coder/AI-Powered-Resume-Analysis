import fitz
# For pdf extraction we use fitz
document=fitz.open("data/SUNIL_RESUME.pdf")
text=""
for page in document:
     text += page.get_text()
print(text) 
document.close()