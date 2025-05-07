from typing import Optional
from pydantic import BaseModel

class PlantEventUpdate(BaseModel):
    plant_id: int = None
    luminosity_event: Optional[float] = None
    humidity_event: Optional[float] = None
    valve_event: Optional[bool] = None
    led_intensity_event: Optional[int] = None
