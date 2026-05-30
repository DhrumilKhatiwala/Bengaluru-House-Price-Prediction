from pydantic import BaseModel
from typing import Optional

class PredictionRequest(BaseModel):
    area_type: str
    availability: str
    location: str
    size: str
    society: Optional[str] = None
    total_sqft: str
    bath: Optional[float] = None
    balcony: Optional[float] = None

class PredictionResponse(BaseModel):
    predicted_price: float
