from sqlalchemy.orm import Session
from sqlalchemy import select
from datetime import datetime, timezone
from models.schema import Log, PlantState, PlantEvent, IotDevState, IotDevEvent, Plant

def insert_new_log_plant(session: Session, plant_id: int):
    try:
        # Get the current time
        now = datetime.now(timezone.utc)

        # Fetch the last temperature value from the Log table
        last_temperature = session.execute(
            select(Log.temperature)
            .where(Log.plant_id == plant_id)
            .order_by(Log.id.desc())
            .limit(1)  # Ensure only one result is returned
        ).scalar_one_or_none()
        print(f"Last temperature for plant ID {plant_id}: {last_temperature}")  
        
        # Fetch the PlantState values for the given plant_id
        plant_state = session.execute(
            select(
                PlantState.luminosity_state,
                PlantState.humidity_state,
                PlantState.valve_state,
                PlantState.led_intensity_state,
                PlantState.mode
            ).where(PlantState.id == session.execute(
                select(Plant.plant_state_id).where(Plant.id == plant_id).limit(1)
            ).scalar_one())
        ).first()
        
        print(f"Plant state for plant ID {plant_id}: {plant_state}")

        # Fetch the PlantEvent values for the given plant_id
        plant_event = session.execute(
            select(
                PlantEvent.luminosity_event,
                PlantEvent.humidity_event,
                PlantEvent.valve_event,
                PlantEvent.led_intensity_event, 
                PlantEvent.mode
            ).where(PlantEvent.id == session.execute(
                select(Plant.plant_event_id).where(Plant.id == plant_id).limit(1)
            ).scalar_one())
        ).first()

        print(f"Plant event for plant ID {plant_id}: {plant_event}")
        
        # Fetch the IotDevState values for the IoT device associated with the plant
        iot_dev_state = session.execute(
            select(IotDevState.pump_state)
            .where(IotDevState.id == session.execute(
                select(Plant.iot_dev_id).where(Plant.id == plant_id).limit(1)
            ).scalar_one())
        ).scalar_one_or_none()

        print(f"IoT device state for plant ID {plant_id}: {iot_dev_state}")
        
        # Fetch the IotDevEvent values for the IoT device associated with the plant
        iot_dev_event = session.execute(
            select(IotDevEvent.pump_event)
            .where(IotDevEvent.id == session.execute(
                select(Plant.iot_dev_id).where(Plant.id == plant_id).limit(1)
            ).scalar_one())
        ).scalar_one_or_none()
        print(f"IoT device event for plant ID {plant_id}: {iot_dev_event}")
        
        # Insert the new log entry
        new_log = Log(
            entry_creation_time=now,
            entry_store_time=now,
            temperature=last_temperature if last_temperature is not None else 0.0,
            luminosity_state=plant_state.luminosity_state,
            humidity_state=plant_state.humidity_state,
            valve_state=plant_state.valve_state,
            led_intensity_state=plant_state.led_intensity_state,
            luminosity_event=plant_event.luminosity_event,
            humidity_event=plant_event.humidity_event,
            valve_event=plant_event.valve_event,
            led_intensity_event=plant_event.led_intensity_event,
            pump_state=iot_dev_state,
            pump_event=iot_dev_event,
            plant_id=plant_id,
            mode_event=plant_event.mode,
            mode_state=plant_state.mode
        )

        session.add(new_log)
        session.commit()
        print(f"New log entry created for plant ID {plant_id}")

    except Exception as e:
        session.rollback()
        print(f"Failed to insert new log entry: {e}")
        raise
    
def insert_new_log_iotDev(session: Session, iot_dev_id: int = None, plant_id: int = 1):
    try:
        # Get the current time
        now = datetime.now(timezone.utc)

        # Fetch the last temperature value from the Log table
        last_temperature = session.execute(
            select(Log.temperature)
            .where(Log.plant_id == plant_id)
            .order_by(Log.id.desc())
            .limit(1)  # Ensure only one result is returned
        ).scalar_one_or_none()
        print(f"Last temperature for plant ID {plant_id}: {last_temperature}")  
        
        # Fetch the PlantState values for the given plant_id
        plant_state = session.execute(
            select(
                PlantState.luminosity_state,
                PlantState.humidity_state,
                PlantState.valve_state,
                PlantState.led_intensity_state,
                PlantState.mode
            ).where(PlantState.id == session.execute(
                select(Plant.plant_state_id).where(Plant.id == plant_id).limit(1)
            ).scalar_one())
        ).first()
        
        print(f"Plant state for plant ID {plant_id}: {plant_state}")

        # Fetch the PlantEvent values for the given plant_id
        plant_event = session.execute(
            select(
                PlantEvent.luminosity_event,
                PlantEvent.humidity_event,
                PlantEvent.valve_event,
                PlantEvent.led_intensity_event,
                PlantEvent.mode
            ).where(PlantEvent.id == session.execute(
                select(Plant.plant_event_id).where(Plant.id == plant_id).limit(1)
            ).scalar_one())
        ).first()

        print(f"Plant event for plant ID {plant_id}: {plant_event}")
        
        # Fetch the IotDevState values for the IoT device from id
        iot_dev_state = session.execute(
            select(IotDevState.pump_state)
            .where(IotDevState.id == iot_dev_id)
        ).scalar_one_or_none()

        print(f"IoT device state ID {plant_id}: {iot_dev_state}")
        
        # Fetch the IotDevEvent values for the IoT device from id
        iot_dev_event = session.execute(
            select(IotDevEvent.pump_event)
            .where(IotDevEvent.id == iot_dev_id)
        ).scalar_one_or_none()
        print(f"IoT device event ID {plant_id}: {iot_dev_event}")
        
        # Insert the new log entry
        new_log = Log(
            entry_creation_time=now,
            entry_store_time=now,
            temperature=last_temperature if last_temperature is not None else 0.0,
            luminosity_state=plant_state.luminosity_state,
            humidity_state=plant_state.humidity_state,
            valve_state=plant_state.valve_state,
            led_intensity_state=plant_state.led_intensity_state,
            luminosity_event=plant_event.luminosity_event,
            humidity_event=plant_event.humidity_event,
            valve_event=plant_event.valve_event,
            led_intensity_event=plant_event.led_intensity_event,
            pump_state=iot_dev_state,
            pump_event=iot_dev_event,
            plant_id=plant_id,
            mode_event=plant_event.mode,
            mode_state=plant_state.mode
        )

        session.add(new_log)
        session.commit()
        print(f"New log entry created for plant ID {plant_id}")

    except Exception as e:
        session.rollback()
        print(f"Failed to insert new log entry: {e}")
        raise