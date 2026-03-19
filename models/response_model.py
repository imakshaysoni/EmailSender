from typing import Optional

from pydantic import BaseModel

class MailHandlerResponse(BaseModel):
    success: bool
    code: int
    status: str
    error_message: str = None

class AuthServiceFailedResponse(BaseModel):
    error_message: str
    user_name: str

class AuthServiceResponseModel(BaseModel):
    success: bool
    message: Optional[str] = None
    id: Optional[int] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None

