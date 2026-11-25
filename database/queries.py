from psycopg.rows import dict_row
from database.connection import get_connection

def get_public_documents() -> list[dict]:
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                "SELECT * FROM public_documents ORDER by id"
            )
            return cursor.fetchall()