from pydantic import BaseModel, EmailStr
from typing import Optional
from fastapi import APIRouter, HTTPException
from domain.Exceptions.MailAlreadySentException import MailAlreadySentException
from domain.Exceptions.EmptyEmailException import EmptyEmailException
from application.send_email_service import SendEmailService


router = APIRouter()
send_email_service = SendEmailService()


class RequestData(BaseModel):
    email: EmailStr
    force_send: Optional[bool] = False


@router.post("/send/single_email")
async def send_single_email_controller(request: RequestData):
    try:
        return send_email_service.send_single_email(request.email, request.force_send)
    except EmptyEmailException:
        raise HTTPException(
            status_code=404,
            detail="Email field required",
        )
    except MailAlreadySentException:
        raise HTTPException(
            status_code=400,
            detail="Email already sent",
        )
