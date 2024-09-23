from pydantic import BaseModel, EmailStr
from datetime import datetime

class Email(BaseModel):

    email_address: EmailStr
    sent_date: datetime
