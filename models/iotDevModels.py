from pydantic import BaseModel

class IoTDevPump(BaseModel):
    iot_dev_id: int = 1
    pump_event: bool = False