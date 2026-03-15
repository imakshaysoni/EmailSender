from models.response_model import MailHandlerResponse
from mail.gmail_mail_sent import GmailMailSent
from models.request_model import MailHandlerRequest, MailLogsRequest
from database.database import Database


class ApiEndpoint:

    @staticmethod
    def mail_handle(request: MailHandlerRequest):
        try:
            db = Database()
            mail_id = db.insert_mail(user_name="Aayush Soni", user_email="soniaayush0044@gmail.com",
                           message=request.message, email_address=request.receiver_email_address)
            mail = GmailMailSent(user_name="Aayush Soni", user_email="soniaayush0044@gmail.com")
            response = mail.sent_mail(data=request)
            if response.status:
                db.update_status(mail_id, True)
            else:
                db.update_status(mail_id, False)
            return response
        except Exception as err:
            error_message = f"Failed to sent email, Error: {err}"
            print(error_message)
            return MailHandlerResponse(
                success=False,
                code=503,
                status="Failed",
                error_message=error_message
            )

    @staticmethod
    def mail_logs(user_email: str):
        try:
            db = Database()
            response = db.get_email_logs(user_email=user_email)
            return response
        except Exception as err:
            print(err)



