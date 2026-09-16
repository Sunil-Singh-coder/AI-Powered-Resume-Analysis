from src.database.save_analysis import save_analysis


analysis_id = save_analysis(
    resume_id=1,
    job_description_id=1,
    skill_score=54.55,
    tfidf_score=19.86,
    semantic_score=45.89,
    final_score=47.62,
    matched_skills=[
        "Python",
        "Flask",
        "Git",
        "GitHub"
    ],
    missing_skills=[
        "FastAPI",
        "PostgreSQL",
        "Docker"
    ],
    ai_recommendation="Focus on FastAPI, PostgreSQL and Docker to improve your backend profile."
)

print("Analysis saved successfully!")
print("Analysis ID:", analysis_id)