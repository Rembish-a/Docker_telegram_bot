from .connection import conn
from psycopg2 import OperationalError


def execute_query(query, connection=conn):
    "Функція, яка приймає рядок query(повинен бути рядком необхідного для виконання SQL-запиту) і об’єкт з’єднання з БД"
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


# Стоврюємо SQL-запит на створення необхідної для нас таблиці
create_message_table = """
CREATE TABLE IF NOT EXISTS message (
    id SERIAL PRIMARY KEY,
    message TEXT,
    userid INTEGER NOT NULL,
    message_time TIMESTAMP WITH TIME ZONE
)
"""

execute_query(create_message_table)


