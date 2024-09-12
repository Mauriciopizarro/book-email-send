from pydantic import BaseModel
from typing import Optional

class Purchase(BaseModel):

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
