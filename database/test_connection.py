from database.connection import get_connection

def main():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT current_database(), current_user;"
            )

            database_name, user = cursor.fetchone()

            print(f"Connected to database: {database_name}")
            print(f"Connected as user: {user}")


if __name__ == "__main__":
    main()
