from src.database.database import get_db_connection


def get_or_create_user(name, email):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Check if user already exists
    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE email = %s;
        """,
        (email,)
    )

    user = cursor.fetchone()

    if user:
        user_id = user[0]

    else:
        cursor.execute(
            """
            INSERT INTO users (name, email)
            VALUES (%s, %s)
            RETURNING id;
            """,
            (name, email)
        )

        user_id = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    return user_id