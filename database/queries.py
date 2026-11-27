from psycopg.rows import dict_row
from database.connection import get_connection

def fetch_public_documents() -> list[dict]:
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                "SELECT * FROM public_documents ORDER by id"
            )
            return cursor.fetchall()

def create_public_documents(title: str, content: str) -> dict:
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                """
                INSERT INTO public_documents (title, content)
                VALUES (%s, %s)
                RETURNING *
                """,
                (title, content)
            )
            return cursor.fetchone()

def update_public_document(
    document_id: int, title: str, content: str
) -> dict | None:
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                """
                UPDATE public_documents
                SET title = %s, content = %s
                WHERE id = %s
                RETURNING *
                """,
                (title, content, document_id)
            )
            return cursor.fetchone()

def delete_public_document(document_id: int) -> bool:
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM public_documents
                WHERE id = %s
                RETURNING id
                """,
                (document_id,)
            )
            return cursor.fetchone() is not None

def fetch_private_documents() -> list[dict]:
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                "SELECT * FROM private_documents ORDER by id",
            )
            return cursor.fetchall()

def create_private_document(
    owner_id: str, title: str, content: str
) -> dict:
    with get_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cursor:
            cursor.execute(
                """
                INSERT INTO private_documents (owner_id, title, content)
                VALUES (%s, %s, %s)
                RETURNING *
                """,
                (owner_id, title, content)
            )
            return cursor.fetchone()