def match_skills(resume_skills, job_skills):

    resume_skills_set = set(resume_skills)
    job_skills_set = set(job_skills)

    matched_skills = resume_skills_set.intersection(job_skills_set)

    missing_skills = job_skills_set - resume_skills_set

    return list(matched_skills), list(missing_skills)


if __name__ == "__main__":

    resume_skills = [
        "Python",
        "Flask",
        "SQL",
        "Git",
        "React"
    ]

    job_skills = [
        "Python",
        "FastAPI",
        "PostgreSQL",
        "Docker",
        "Git"
    ]

    matched, missing = match_skills(
        resume_skills,
        job_skills
    )

    print("----- MATCHED SKILLS -----")

    for skill in matched:
        print("-", skill)

    print("\n----- MISSING SKILLS -----")

    for skill in missing:
        print("-", skill)