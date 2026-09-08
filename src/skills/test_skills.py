from src.skills.skils_dictionary import SKILLS

text= " i am sunil i have developed different skills python ,django,java and i also " \
"have knowledge in GIT machine learning js ml "

found_skills= []

for skill in SKILLS :
    if skill.lower() in text.lower():
        found_skills.append(skill)

print(found_skills)
