import uuid
from datetime import datetime

from config.config import DATABASE_NAME
from database.postgress import get_connection

from database.database_model import Users


class Database:

    def __init__(self):
        self.conn = get_connection(db_name=DATABASE_NAME)
        self.conn.autocommit = True
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

    def get_user(self, user_name: str):
        query = """
            select id, user_name, user_email, password from users where user_name=%s
        """
        self.cursor.execute(query, (user_name,))

        user_details = self.cursor.fetchone()
        if user_details:
           return Users(id=user_details[0], user_name=user_details[1], email_address=user_details[2], password=user_details[3])
        else:
            return Users()

    def insert_user(self, user_name: str, password, email_address):
        query = """
            INSERT INTO users (user_name, user_email, password)
            VALUES (%s, %s, %s)
            RETURNING id
        """
        self.cursor.execute(query, (user_name, email_address, password))
        user_id = self.cursor.fetchone()
        return user_id[0]

    def reset_password(self, user_name: str, password: str):
        # update new password in database
        query = """
            update users set password=%s where user_name=%s
        """

        self.cursor.execute(query, (password,user_name))

    def get_token_from_db(self, jti: str):
        query = """
            select user_name, is_revoked from refresh_token where jti=%s 
        """
        self.cursor.execute(query, (jti, ))
        response = self.cursor.fetchone()
        if response:
            return response[0], response[1]
        return None, None

    def save_refresh_token(self, data: dict):
        print(data)
        user_name  = data["sub"]
        type = data["type"]
        expire = data["exp"]
        jti = data["jti"]

        query = """
            insert into refresh_token (user_name, type, jti, expire) values (%s, %s, %s, %s)
        """
        self.cursor.execute(query, (user_name, type, jti, expire))
        return







    def close_connection(self):
        self.cursor.close()
        self.conn.close()

