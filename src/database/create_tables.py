from src.database.database import get_db_connection


def create_tables():

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(150) UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resumes (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            file_name VARCHAR(255),
            resume_text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_descriptions (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            job_title VARCHAR(150),
            job_description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id SERIAL PRIMARY KEY,
            resume_id INTEGER REFERENCES resumes(id),
            job_description_id INTEGER REFERENCES job_descriptions(id),
            skill_score FLOAT,
            tfidf_score FLOAT,
            semantic_score FLOAT,
            final_score FLOAT,
            matched_skills TEXT,
            missing_skills TEXT,
            ai_recommendation TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    connection.commit()

    cursor.close()
    connection.close()

    print("All tables created successfully!")


if __name__ == "__main__":
    create_tables()