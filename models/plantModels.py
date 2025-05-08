from typing import Optional
from pydantic import BaseModel

class PlantEventUpdate(BaseModel):
    plant_id: int = None
    mode: int = None  # The mode of the plant
    luminosity_event: Optional[float] = None
    humidity_event: Optional[float] = None
    valve_event: Optional[bool] = None
    led_intensity_event: Optional[int] = None

class InsertLogRequest(BaseModel):
    plant_id: int  # The ID of the plant for which the log entry is being created
    
