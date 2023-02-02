import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import OperationalError, connect
import os

con = psycopg2.connect("user=postgres password='postgres' host=bot_db port=5432")
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = con.cursor()
cursor.execute("CREATE DATABASE dbbot;")












# name = os.environ["DB_NAME"]
# user = os.environ["POSTGRES_USER"]
# password = os.environ["POSTGRES_PASSWORD"]
# host = os.environ["DB_HOST"]
# port = os.environ["DB_PORT"]
#
#
# def create_connection(
#     db_name=name,
#     db_user=user,
#     db_password=password,
#     db_host=host,
#     db_port=port
# ):
#     try:
#         print("try connection...")
#         connection = connect(
#             database=db_name,
#             user=db_user,
#             password=db_password,
#             host=db_host,
#             port=db_port,
#         )
#         print("Connection to PostgreSQL DB successful")
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#         connection = None
#     return connection
#
#
# conn = create_connection()

