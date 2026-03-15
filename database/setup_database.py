from postgress import get_connection


def init_db():

    # connect to default postgres DB
    conn = get_connection("postgres")
    conn.autocommit = True
    cursor = conn.cursor()

    # check if database exists
    cursor.execute(
        "SELECT 1 FROM pg_database WHERE datname='notify_service'"
    )

    exists = cursor.fetchone()

    if not exists:
        cursor.execute("CREATE DATABASE notify_service")
        print("Database created")

    cursor.close()
    conn.close()

    # connect to notify_service database
    conn = get_connection("notify_service")
    cursor = conn.cursor()

    # create table
    query = """
    CREATE TABLE IF NOT EXISTS email_records (
        id SERIAL PRIMARY KEY,
        user_name VARCHAR(50) NOT NULL,
        user_email VARCHAR(100) NOT NULL,
        message TEXT NOT NULL,
        receiver_email_address VARCHAR(50) NOT NULL,
        status BOOLEAN NOT NULL DEFAULT FALSE,
        sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

    print("Table created successfully")


if __name__ == "__main__":
    init_db()