from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter, HTTPException, Depends
from application.save_purchase_service import SavePurchaseService
from infrastructure.injector import Injector
from dependency_injector.wiring import Provide, inject


router = APIRouter()

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
@inject
async def save_purchase_controller(save_request_data: SavePurchaseRequestData,
                                   save_purchase_service = Depends(Provide[Injector.save_purchase_service])):
    save_purchase_service.save_purchase(save_request_data.__dict__)
