from pydantic import BaseModel, validator, EmailStr
from fastapi import APIRouter, HTTPException
from domain.Exceptions import EmptyEmailException
from application.send_email_service import SendEmailService


router = APIRouter()
send_email_service = SendEmailService()


class RequestData(BaseModel):
    email: str


@router.post("/send/single_email")
async def send_single_email_controller(request: RequestData):
    try:
        return send_email_service.send_single_email(request.email)
    except EmptyEmailException:
        raise HTTPException(
            status_code=404,
            detail="Email field required",
        )
