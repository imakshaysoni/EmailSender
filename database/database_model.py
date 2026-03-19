# from datetime import datetime
from optparse import Option
from types import NoneType
from typing import Optional

from pydantic import BaseModel
#
# class EmailRecords():
#     id: int
#     user_name: str
#     user_email: str
#     message: str
#     email_address: str
#     sent_at: datetime

class Users(BaseModel):
    id: Optional[int] = None
    user_name: Optional[str] = None
    email_address: Optional[str] = None
    password: Optional[str] = None