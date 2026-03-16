import uvicorn
import psycopg2
from fastapi import FastAPI

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI()


######## Database ##################

def get_connection(db_name):
    conn = psycopg2.connect(
        host="localhost",
        database=db_name,
        user="postgres",
        password="postgres",
        port=5432
    )
    return conn
######### Functions ##############
def create_message(user_email, receiver_email_address, message):
    msg = MIMEMultipart()
    msg["From"] = user_email
    msg["To"] = receiver_email_address
    msg["Subject"] = "subject"

    msg.attach(MIMEText(message, "plain"))
    return msg


def setup_smtp_server(user_email):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user_email, "bpwy exxc nkkn eofg")
    return server


def get_email_logs(user_email: str):
    conn = get_connection(db_name="notify_service")
    cursor = conn.cursor()
    query = """ select * from email_records where user_email=%s """
    cursor.execute(query, (user_email,))

    response = cursor.fetchall()

    print(response)
    return response

############ Endpoints ################
@app.post("/sent_mail")
def mail_sent(message, receiver_email_address):
    try:
        print(f"Sending Message {message} to user {receiver_email_address}")
        user_email="soniaayush0044@gmail.com"
        msg = create_message(user_email=user_email,
                             receiver_email_address=receiver_email_address, message=message)
        server = setup_smtp_server(user_email=user_email)

        # sending mail
        server.sendmail(user_email, receiver_email_address, msg.as_string())
        server.quit()
        print("Email sent succesfully")
        return "Email sent successfully"
    except Exception as err:
        print(f"Error: {err}")
        return f"Error: {err}"


@app.get("/mail_logs")
def get_mail_log(user_email):
    try:
        response = get_email_logs(user_email=user_email)
        return response
    except Exception as err:
        print(f"Error: {err}")
        return f"Error: {err}"



if __name__=="__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)