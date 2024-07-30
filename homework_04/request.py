import psycopg2
from psycopg2 import OperationalError


def create_connection():
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="user",
            password="password",
            host="localhost",
            port="5432"
        )
        print("Connection to PostgreSQL DB successful")
        return connection
    except OperationalError as e:
        print(f"The error '{e}' occurred")

connection = create_connection()