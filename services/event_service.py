from sqlalchemy.orm import Session
from sqlalchemy import update
from datetime import datetime, timezone
from models.schema import PlantEvent, IotDevEvent

def update_plant_event(session: Session, event_type: str, event_value, event_id: int):
    stmt = (
        update(PlantEvent)
        .where(PlantEvent.id == event_id)
        .values({event_type: event_value, "last_updated": datetime.now(timezone.utc)})
    )
    session.execute(stmt)
    print(f"Updating {event_type} for plant ID {event_id} to {event_value}")
    session.commit()
    print(f"Updated {event_type} for plant ID {event_id} to {event_value}")

def update_device_event(session: Session, event_value: bool, event_id: int):
    stmt = (
        update(IotDevEvent)
        .where(IotDevEvent.id == event_id)
        .values(pump_event=event_value, last_updated=datetime.now(timezone.utc))
    )
    session.execute(stmt)
    print(f"Updating pump event for device ID {event_id} to {event_value}")
    session.commit()
    print(f"Updated pump event for device ID {event_id} to {event_value}")
