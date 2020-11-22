import psycopg2


def connect():
    # Connect to an existing database
    conn = psycopg2.connect(
        host="localhost", dbname="todoTask", user="postgres", password="postgres")

    return conn
