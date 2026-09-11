from pathlib import Path

from src.extraction.resume_parser import extract_text_from_pdf
from src.extraction.jd_parser import extract_text_from_jd
from src.preprocessing.text_cleaner import clean_text
from src.skills.skill_extractor import extract_skills
from src.matching.skill_matcher import generate_skill_gap, calculate_match_score,calculate_final_score
from src.matching.tfidf_similarity import calculate_tfidf_similiarity
from src.matching.semantic_similarity import calculate_semantic_similarity




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
    resume_skill_text = " ".join(resume_skills)
    job_skill_text = " ".join(job_skills)

    # match resume skills and jd skills 
    skills_gap= generate_skill_gap(
        resume_skills,
        job_skills
    )


    # -------------------------
    # 5. Calculate skills Score
    # -------------------------
    skill_score = calculate_match_score(
        resume_skills,
        job_skills
    )
        # -------------------------
    # 6. Calculate similarity 
    # -------------------------
    tfidf_score=calculate_tfidf_similiarity(resume_text,jd_text)

         # -------------------------
         # 7. Calculate similarity 
         # -------------------------

    semantic_score = calculate_semantic_similarity(
    resume_text,
    jd_text
)

       # -------------------------
    # 8. Calculate final
    # -------------------------
    final_score = calculate_final_score(
    skill_score,
    semantic_score,
    tfidf_score
)


    return {
    "resume_skills": resume_skills,
    "job_skills": job_skills,

    "skill_analysis": {
        "matched_skills": skills_gap["matched_skills"] ,
        "missing_skills": skills_gap["missing_skills"],
        "total_required_skills": skills_gap["total_required_skills"],
        "total_matched_skills": skills_gap["total_matched_skills"],
        "total_missing_skills": skills_gap["total_missing_skills"]
    },

    "scores": {
        "skill_score": float(skill_score),
        "tfidf_score": float(tfidf_score),
        "semantic_score": float(semantic_score),
        "final_score": float(final_score)
    }
}


if __name__ == "__main__":

    BASE_DIR = Path(__file__).resolve().parents[2]

    resume_path = BASE_DIR / "data" / "resumes" / "Afreen_Khatoon_Resume.pdf"

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

    print(f"Total required skills { result["skills_gap"]["total_required_skills"]} ")  
    print(f"Total matched skills { result["skills_gap"]["total_matched_skills"]} ")  
    print(f"Total missing skills { result["skills_gap"]["total_missing_skills"]}")  
     


    print("\nSkill Match Score:")
    print(f'{result["skill_score"]}%')

    print("\nTF-IDF Similarity Score:")
    print(f'{result["tfidf_score"]}%')

    print("\n Semantic score Similarity Score:")
    print(f'{result["semantic_score"]}%')

    print("\nFinal Match Score:")
    print(f'{result["final_score"]}%')




    





