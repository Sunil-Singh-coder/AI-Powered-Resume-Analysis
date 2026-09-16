from src.database.database import get_db_connection


def save_resume(user_id, file_name, resume_text):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO resumes (user_id, file_name, resume_text)
        VALUES (%s, %s, %s)
        RETURNING id;
        """,
        (user_id, file_name, resume_text)
    )

    resume_id = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return resume_id