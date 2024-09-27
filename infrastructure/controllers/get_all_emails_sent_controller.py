from typing import List
from fastapi import APIRouter, Depends
from datetime import datetime
from infrastructure.injector import Injector
from dependency_injector.wiring import Provide, inject
from pydantic import BaseModel, EmailStr
from application.get_all_emails_sent_service import AllEmailsSentService


router = APIRouter()


class ResponseModelData(BaseModel):
    date: datetime
    email: EmailStr


@router.get("/email/all_sent", response_model=List[ResponseModelData])
@inject
async def get_all_emails_sent(all_emails_service = Depends(Provide[Injector.get_all_emails_service])):
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
