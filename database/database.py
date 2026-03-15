from datetime import datetime

from config.postgress import DATABASE_NAME
from database.postgress import get_connection


class Database:

    def __init__(self):
        self.conn = get_connection(db_name=DATABASE_NAME)
        self.cursor = self.conn.cursor()

    def insert_mail(self, user_name, user_email, message, email_address):
        query = """
        INSERT INTO email_records (user_name, user_email, message, receiver_email_address)
        VALUES (%s, %s, %s, %s) RETURNING id
        """

        self.cursor.execute(query, (user_name, user_email, message, email_address))

        self.conn.commit()
        response = self.cursor.fetchone()
        return response[0]

    def update_status(self, mail_id, status):
        query = f"update email_records set status={status} where id={mail_id}"
        self.cursor.execute(query)
        self.conn.commit()

    def get_email_logs(self, user_email: str):
        query = """ select * from email_records where user_email=%s """
        self.cursor.execute(query, (user_email,))

        response = self.cursor.fetchall()

        print(response)
        return response


    def close_connection(self):
        self.cursor.close()
        self.conn.close()

