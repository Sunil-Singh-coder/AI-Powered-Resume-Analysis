from src.database.database import get_db_connection


def save_analysis(
    resume_id,
    job_description_id,
    skill_score,
    tfidf_score,
    semantic_score,
    final_score,
    matched_skills,
    missing_skills,
    ai_recommendation
):

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO analyses (
            resume_id,
            job_description_id,
            skill_score,
            tfidf_score,
            semantic_score,
            final_score,
            matched_skills,
            missing_skills,
            ai_recommendation
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
        """,
        (
            resume_id,
            job_description_id,
            skill_score,
            tfidf_score,
            semantic_score,
            final_score,
            ", ".join(matched_skills),
            ", ".join(missing_skills),
            ai_recommendation
        )
    )

    analysis_id = cursor.fetchone()[0]

    connection.commit()

    cursor.close()
    connection.close()

    return analysis_id