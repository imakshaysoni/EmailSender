from pydantic import BaseModel

class MailHandlerRequest(BaseModel):
    message: str
    receiver_email_address: str

class MailLogsRequest(BaseModel):
    user_email: str


class LoginDetails(BaseModel):
    user_name: str
    password: str

class SignUpDetails(BaseModel):
    user_name: str
    email_address: str
    password: str

class ResetPasswordDetails(BaseModel):
    user_name: str


class RefreshToken(BaseModel):
    refresh_token: str