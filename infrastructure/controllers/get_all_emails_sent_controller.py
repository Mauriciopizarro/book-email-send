from typing import List
from fastapi import APIRouter
from datetime import datetime
from pydantic import BaseModel, EmailStr
from application.get_all_emails_sent_service import AllEmailsSentService


router = APIRouter()
all_emails_service = AllEmailsSentService()


class ResponseModelData(BaseModel):
    date: datetime
    email: EmailStr


@router.get("/email/all_sent", response_model=List[ResponseModelData])
async def get_all_emails_sent():
    data = all_emails_service.get_all_emails_sent()
    response_list = []
    for email_sent in data:
        response_list.append(
            {
                "date": email_sent.get('sent_date'),
                "email": email_sent.get('email_address')
            }
        )
    return response_list
