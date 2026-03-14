from pydantic import BaseModel

class MailHandlerResponse(BaseModel):
    success: bool
    code: int
    status: str
    error_message: str = None