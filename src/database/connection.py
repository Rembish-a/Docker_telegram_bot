import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import OperationalError, connect
import os

# con = psycopg2.connect("user=postgres password='postgres' host=bot_db port=5432")
# con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor = con.cursor()
# cursor.execute("CREATE DATABASE dbbot;")

# За допомогою модуля os прочитали всі необхідні нам для підключення до БД параметри із змінних середовища. В файлі
# docker-compose.yaml коли задані значення для змінних оточення

name = os.environ["DB_NAME"]
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
host = os.environ["DB_HOST"]
port = os.environ["DB_PORT"]


def create_connection(
    db_name=name,
    db_user=user,
    db_password=password,
    db_host=host,
    db_port=port
):
    "Функція, яка за замовченням приймає параметри прочитані із змінного оточення і створює об’єкт psycopg2.connect"
    try:
        print("try connection...")
        connection = connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
        connection = None
    return connection


conn = create_connection()               #створюємо об’єкт з’єднання

