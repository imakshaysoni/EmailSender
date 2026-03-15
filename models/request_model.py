from pydantic import BaseModel

class MailHandlerRequest(BaseModel):
    message: str
    receiver_email_address: str

class MailLogsRequest(BaseModel):
    user_email: str
