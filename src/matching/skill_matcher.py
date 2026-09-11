from src.skills.jd_skill_config import REQUIRED_SKILL_GROUPS

def generate_skill_gap(resume_skills, job_skills):
    resume_skills_set = set(resume_skills)
    job_skills_set = set(job_skills)

    matched_skills = sorted(
        resume_skills_set.intersection(job_skills_set)
    )

    missing_skills = sorted(
        job_skills_set - resume_skills_set
    )

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "total_required_skills": len(job_skills_set),
        "total_matched_skills": len(matched_skills),
        "total_missing_skills": len(missing_skills)
    }
def calculate_match_score(resume_skills, job_skills):

    if not job_skills:
        return 0

    skills_gap = generate_skill_gap(
        resume_skills,
        job_skills
    )

    score = (len(skills_gap["matched_skills"]) / len(job_skills)) * 100

    return round(score, 2)

def calculate_final_score(
    skill_score,
    semantic_score,
    tfidf_score):
    final_score = (
        (skill_score * 0.50)
        +
        (semantic_score * 0.40)
        +
        (tfidf_score * 0.10)
    )

    return round(final_score, 2)

# match skills with or & and concept 
def match_skill_groups(resume_skills, required_skill_groups):

    resume_skills_set = set(resume_skills)

    matched_groups = []
    missing_groups = []

    for group in required_skill_groups:

        group_type = group["type"]
        skills = group["skills"]

        if group_type == "single":

            if skills[0] in resume_skills_set:
                matched_groups.append(group)
            else:
                missing_groups.append(group)

        elif group_type == "or":

            if any(skill in resume_skills_set for skill in skills):
                matched_groups.append(group)
            else:
                missing_groups.append(group)

        elif group_type == "and":

            if all(skill in resume_skills_set for skill in skills):
                matched_groups.append(group)
            else:
                missing_groups.append(group)

    return matched_groups, missing_groups

if __name__ == "__main__":

    resume_skills = [
        "Python",
        "Flask",
        "SQL",
        "Git",
        "GitHub"
    ]

    # required_skill_groups = [
    #     ["Python"],
    #     ["FastAPI", "Flask"],
    #     ["SQL", "PostgreSQL"],
    #     ["REST API"],
    #     ["Git", "GitHub"],
    #     ["Docker"]
    # ]

    matched, missing = match_skill_groups(
        resume_skills,
        REQUIRED_SKILL_GROUPS
    )

    print("Matched Groups:")
    for group in matched:
        print("-", group)

    print("\nMissing Groups:")
    for group in missing:
        print("-", group)