# This structure we are followed to extract the skills from pdf only 
# Resume PDF
#      ↓
# PyMuPDF
#      ↓
# Text Cleaning
#      ↓
# spaCy
#      ↓
# PhraseMatcher
#      ↓
# Skill Detection
#      ↓
# Alias Normalization
#      ↓


import spacy
from spacy.matcher import PhraseMatcher

from src.skills.skill_dictionary import SKILLS, SKILL_ALIASES


nlp = spacy.load("en_core_web_sm")

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")


# Main skills
skill_patterns = [
    nlp.make_doc(skill)
    for skill in SKILLS
]

matcher.add("SKILLS", skill_patterns)


# Aliases
alias_patterns = [
    nlp.make_doc(alias)
    for alias in SKILL_ALIASES
]

matcher.add("ALIASES", alias_patterns)


def extract_skills(text):

    doc = nlp(text)

    matches = matcher(doc)

    found_skills = []

    for match_id, start, end in matches:

        matched_text = doc[start:end].text

        match_name = nlp.vocab.strings[match_id]

        if match_name == "SKILLS":

            standard_skill = matched_text

        else:

            standard_skill = SKILL_ALIASES.get(
                matched_text.lower()
            )

        if standard_skill and standard_skill not in found_skills:

            found_skills.append(standard_skill)

    return found_skills

# For  Testing pupuse 
# if __name__ == "__main__":

#     text = """
#     I have experience in Python, ML, NLP, Postgres,
#     ReactJS, JS and Flask.
#     """

#     skills = extract_skills(text)

#     print("Detected Skills:")

#     for skill in skills:
#         print("-", skill)