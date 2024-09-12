from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, HTTPException
from application.save_purchase_service import SavePurchaseService


router = APIRouter()
save_purchase_service = SavePurchaseService()

class SavePurchaseRequestData(BaseModel):
    identification_number: int
    phone_number: str
    name: str
    last_name: str
    country: str
    city: str
    street: str
    street_number: int
    zip_code: int
    reference: Optional[str] = None



@router.post("/save/purchase")
async def save_purchase_controller(save_request_data: SavePurchaseRequestData):
    save_purchase_service.save_purchase(save_request_data.__dict__)
