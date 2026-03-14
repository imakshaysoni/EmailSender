from pydantic import BaseModel

class MailHandlerRequest(BaseModel):
    message: str
    receiver_email_address: str