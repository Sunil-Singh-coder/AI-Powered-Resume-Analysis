def match_skills(resume_skills, job_skills):

    resume_skills_set = set(resume_skills)
    job_skills_set = set(job_skills)

    matched_skills = resume_skills_set.intersection(job_skills_set)

    missing_skills = job_skills_set - resume_skills_set

    return list(matched_skills), list(missing_skills)

def calculate_match_score(resume_skills, job_skills):

    if not job_skills:
        return 0

    matched_skills, missing_skills = match_skills(
        resume_skills,
        job_skills
    )

    score = (len(matched_skills) / len(job_skills)) * 100

    return round(score, 2)

def calculate_final_score(skill_score, tfidf_score):

    final_score = (
        (skill_score * 0.70)
        +
        (tfidf_score * 0.30)
    )

    return round(final_score, 2)

# if __name__ == "__main__":

#     resume_skills = [
#         "Python",
#         "Flask",
#         "SQL",
#         "Git",
#         "React"
#     ]

#     job_skills = [
#         "Python",
#         "FastAPI",
#         "PostgreSQL",
#         "Docker",
#         "Git"
#     ]

#     matched, missing = match_skills(
#         resume_skills,
#         job_skills
#     )
#     score = calculate_match_score(
#         resume_skills,
#         job_skills
#     )
 

#     print("----- MATCHED SKILLS -----")

#     for skill in matched:
#         print("-", skill)

#     print("\n----- MISSING SKILLS -----")

#     for skill in missing:
#         print("-", skill)


#     print("\n----- MATCH SCORE -----")
#     print(f"Score: {score}%")    

if __name__ == "__main__":

    skill_score = 40.0
    tfidf_score = 51.01

    final_score = calculate_final_score(
        skill_score,
        tfidf_score
    )

    print("Skill Match Score:", skill_score, "%")
    print("TF-IDF Similarity:", tfidf_score, "%")
    print("Final Match Score:", final_score, "%")    