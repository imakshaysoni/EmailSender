from models.response_model import MailHandlerResponse
from mail.gmail_mail_sent import GmailMailSent
from models.request_model import MailHandlerRequest, MailLogsRequest
from database.database import Database
from models.request_model import SignUpDetails, LoginDetails, \
    ResetPasswordDetails
from services.auth_service import AuthService
from fastapi import Depends

from config.config import TokenData

from models.request_model import RefreshToken


class ApiEndpoint:
    @staticmethod
    def mail_handle(request: MailHandlerRequest, user = Depends(AuthService.get_current_user)):
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
    def mail_logs(user_email: str, user = Depends(AuthService.get_current_user)):
        try:
            db = Database()
            response = db.get_email_logs(user_email=user_email)
            return response
        except Exception as err:
            print(err)


class AuthServiceEndpoint:

    @staticmethod
    def login(request: LoginDetails):
        auth_service = AuthService()
        response = auth_service.login(user_name=request.user_name, password=request.password)
        return response

    @staticmethod
    def signup(request: SignUpDetails):
        auth_service = AuthService()
        response = auth_service.sign_up(user_name=request.user_name, password=request.password, email_address=request.email_address)
        return response


    @staticmethod
    def reset_password(request: ResetPasswordDetails):
        auth_service = AuthService()
        response = auth_service.reset_password(user_name=request.user_name)
        return response

    @staticmethod
    def refresh_token(request: RefreshToken):
        auth_service = AuthService()
        response = auth_service.refresh_access_token(refresh_token=request.refresh_token)
        return response

