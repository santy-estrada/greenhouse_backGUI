from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils.db import get_session
from services.event_service import update_plant_event, update_device_event
from models.plantModels import PlantEventUpdate
from models.iotDevModels import IoTDevPump
from models.schema import PlantEvent, IotDevEvent
from fastapi import HTTPException, status
from utils.request_validation import check_plant_event_exists, check_iot_dev_event_exists
from utils.request_validation import validate_not_none, validate_positive_integer, validate_float, validate_range, validate_boolean
router = APIRouter(prefix="/events", tags=["Events"])

@router.put("/plant/luminosity")
def update_luminosity_event(data: PlantEventUpdate, session: Session = Depends(get_session)):
    try:
        validate_not_none(data.luminosity_event, "Luminosity event cannot be None.")
        validate_not_none(data.plant_id, "Plant ID cannot be None.")
        validate_positive_integer(data.plant_id, "Plant ID must be a positive integer.")    
        validate_float(data.luminosity_event, "Luminosity event must be a float.")
        validate_range(data.luminosity_event, 0, 100, "Luminosity event must be between 0 and 100.")
        check_plant_event_exists(session, data.plant_id)

        update_plant_event(session, "luminosity_event", data.luminosity_event, data.plant_id)
        return {"message": "Luminosity event updated", "plant_id": data.plant_id, "luminosity_event": data.luminosity_event}
    except HTTPException as e:
        raise e
    except Exception as e:
         raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ocurrió un error en el servidor: " + str(e)
        )
         
         
@router.put("/plant/humidity")
def update_humidity_event(data: PlantEventUpdate, session: Session = Depends(get_session)):
    validate_not_none(data.humidity_event, "Humidity event cannot be None.")
    validate_not_none(data.plant_id, "Plant ID cannot be None.")
    validate_positive_integer(data.plant_id, "Plant ID must be a positive integer.")
    validate_float(data.humidity_event, "Humidity event must be a float.")
    validate_range(data.humidity_event, 0, 100, "Humidity event must be between 0 and 100.")
    check_plant_event_exists(session, data.plant_id)
    
    update_plant_event(session, "humidity_event", data.humidity_event, data.plant_id)
    return {"message": "Humidity event updated", "plant_id": data.plant_id, "humidity_event": data.humidity_event}

@router.put("/plant/valve")
def update_valve_event(data: PlantEventUpdate, session: Session = Depends(get_session)):
    validate_not_none(data.valve_event, "Valve event cannot be None.")
    validate_not_none(data.plant_id, "Plant ID cannot be None.")
    validate_positive_integer(data.plant_id, "Plant ID must be a positive integer.")
    validate_boolean(data.valve_event, "Valve event must be a boolean.")
    check_plant_event_exists(session, data.plant_id)
    
    update_plant_event(session, "valve_event", data.valve_event, data.plant_id)
    return {"message": "Valve event updated", "plant_id": data.plant_id, "valve_event": data.valve_event}

@router.put("/plant/led")
def update_led_event(data: PlantEventUpdate, session: Session = Depends(get_session)):
    validate_not_none(data.led_intensity_event, "LED event cannot be None.")
    validate_not_none(data.plant_id, "Plant ID cannot be None.")
    validate_positive_integer(data.plant_id, "Plant ID must be a positive integer.")
    validate_range(data.led_intensity_event, 0, 100, "LED event must be between 0 and 100.")
    check_plant_event_exists(session, data.plant_id)

    update_plant_event(session, "led_intensity_event", data.led_intensity_event, data.plant_id)
    return {"message": "LED intensity event updated", "plant_id": data.plant_id, "led_intensity_event": data.led_intensity_event}

@router.put("/device/pump")
def update_pump_event(data: IoTDevPump, session: Session = Depends(get_session)):
    validate_not_none(data.pump_event, "Pump event cannot be None.")
    validate_not_none(data.iot_dev_id, "IoT Device ID cannot be None.")
    validate_positive_integer(data.iot_dev_id, "IoT Device ID must be a positive integer.")
    validate_boolean(data.pump_event, "Pump event must be a boolean.")
    check_iot_dev_event_exists(session, data.iot_dev_id)
    
    update_device_event(session, data.pump_event, data.iot_dev_id)
    return {"message": "Pump event updated", "iot_dev_id": data.iot_dev_id, "pump_event": data.pump_event}
