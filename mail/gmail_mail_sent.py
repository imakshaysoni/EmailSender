from mail.base_mail import SentMail
from models.response_model import MailHandlerResponse
from models.request_model import MailHandlerRequest


class GmailMailSent(SentMail):

    def __init__(self, user_name, user_email):
        self.user_name = user_name
        self.user_email = user_email

    def sent_mail(self, data: MailHandlerRequest):
        print(f"Sending Message {data.message} to user {data.receiver_email_address}")
        return MailHandlerResponse(
            success=True,
            code=200,
            status="Success",
            error_message=""
        )
