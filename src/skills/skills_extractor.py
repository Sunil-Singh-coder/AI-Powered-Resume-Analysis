from src.skills.skils_dictionary import SKILLS,SKILL_ALIASES


def extract_skills(text):
    text_lower=text.lower()
    found_skills= []
    for skill in SKILLS :
       if skill.lower() in text_lower:
          found_skills.append(skill)

    for alias, standard_skill in SKILL_ALIASES.items():
        if alias in text_lower:
            if standard_skill not in found_skills:
                found_skills.append(standard_skill)


    return found_skills      