from src.database.database import get_db_connection


try:
    connection = get_db_connection()

    print("Database connected successfully!")

    connection.close()

except Exception as e:
    print("Database connection failed:")
    print(e)