from src.database.database import get_db_connection


def save_job_description(user_id, job_title, job_description):
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO job_descriptions (user_id, job_title, job_description)
        VALUES (%s, %s, %s)
        RETURNING id;
        """,
        (user_id, job_title, job_description)
    )

    job_description_id = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return job_description_id