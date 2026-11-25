import psycopg

from database.connection import get_connection

def main():
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT current_database(), current_user;"
                )

                database_name, user = cursor.fetchone()

                print(f"Connected to database: {database_name}")
                print(f"Connected as user: {user}")
    
    except psycopg.OperationalError as e:
        print(f"Database connection failed: {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
