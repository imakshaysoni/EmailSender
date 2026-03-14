from models.response_model import MailHandlerResponse
from mail.gmail_mail_sent import GmailMailSent
from models.request_model import MailHandlerRequest

class ApiEndpoint:

    @staticmethod
    def mail_handle(request: MailHandlerRequest):
        try:
            mail = GmailMailSent(user_name="Aayush Soni", user_email="soniaayush0044@gmail.com")
            response = mail.sent_mail(data=request)
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



