from fastapi import APIRouter, Depends
from pydantic import BaseModel, EmailStr
from typing import List
from infrastructure.injector import Injector
from dependency_injector.wiring import Provide, inject
from application.send_bulk_email_service import SendBulkEmailService


router = APIRouter()

class EmailRequest(BaseModel):
    email: EmailStr

class ListEmailRequest(BaseModel):
    email_list: List[EmailRequest]


@router.post("/send/bulk_email")
@inject
async def send_bulk_email_controller(request: ListEmailRequest, bulk_email_service = Depends(Provide[Injector.send_bulk_email_service])):
    await bulk_email_service.send_bulk_email(request.email_list)
    return {
        'response': "200 OK"
    }