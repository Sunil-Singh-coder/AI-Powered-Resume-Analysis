from pathlib import Path

from src.extraction.resume_parser import extract_text_from_pdf
from src.extraction.jd_parser import extract_text_from_jd
from src.preprocessing.text_cleaner import clean_text
from src.skills.skill_extractor import extract_skills
from src.matching.skill_matcher import match_skills, calculate_match_score


def analyze_resume(resume_path,jd_path):

    # extract resume text 
    resume_text=extract_text_from_pdf(resume_path)
    resume_text=clean_text(resume_text)

    # extrct hd text 
    jd_text=extract_text_from_jd(jd_path)
    jd_text=clean_text(jd_text)

    # extract skills from resume and job discription 
    resume_skills=extract_skills(resume_text)
    job_skills=extract_skills(jd_text)

    # match resume skills and jd skills 
    matched_skills, missing_skills = match_skills(
        resume_skills,
        job_skills
    )


    # -------------------------
    # 5. Calculate Score
    # -------------------------
    score = calculate_match_score(
        resume_skills,
        job_skills
    )
    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": score
    }


if __name__ == "__main__":

    BASE_DIR = Path(__file__).resolve().parents[2]

    resume_path = BASE_DIR / "data" / "resumes" / "Resume_ML.pdf"

    jd_path = BASE_DIR / "data" / "job_descriptions" / "job1.txt"


    result = analyze_resume(
        resume_path,
        jd_path
    )


    print("\n========== AI RESUME ANALYSIS ==========\n")


    print("Resume Skills:")
    for skill in result["resume_skills"]:
        print("-", skill)


    print("\nJob Required Skills:")
    for skill in result["job_skills"]:
        print("-", skill)


    print("\nMatched Skills:")
    for skill in result["matched_skills"]:
        print("-", skill)


    print("\nMissing Skills:")
    for skill in result["missing_skills"]:
        print("-", skill)


    print("\nMatch Score:")
    print(f'{result["match_score"]}%')


    





