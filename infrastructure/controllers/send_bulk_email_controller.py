from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import List
from application.send_bulk_email_service import SendBulkEmailService


router = APIRouter()
bulk_email_service = SendBulkEmailService()

class EmailRequest(BaseModel):
    email: EmailStr

class ListEmailRequest(BaseModel):
    email_list: List[EmailRequest]


@router.post("/send/bulk_email")
async def send_bulk_email_controller(request: ListEmailRequest):
    await bulk_email_service.send_bulk_email(request.email_list)
    return {
        'response': "200 OK"
    }