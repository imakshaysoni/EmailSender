import psycopg2

def get_connection(db_name):
    conn = psycopg2.connect(
        host="localhost",
        database=db_name,
        user="postgres",
        password="postgres",
        port=5432
    )
    return conn