from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.schema import PlantEvent, IotDevEvent

def validate_not_none(value, field_name: str):
    """Validate that a value is not None."""
    if value is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} cannot be None."
        )

def validate_positive_integer(value, field_name: str):
    """Validate that a value is a positive integer."""
    if not isinstance(value, int) or value <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} must be a positive integer."
        )
        
def validate_float(value, field_name: str):
    """Validate that a value is a float."""
    if not isinstance(value, float):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} must be a float."
        )

def validate_range(value, min_value: int, max_value: int, field_name: str):
    """Validate that a value is within a specific range."""
    if not isinstance(value, (int, float)) or value < min_value or value > max_value:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} must be between {min_value} and {max_value}."
        )

def validate_boolean(value, field_name: str):
    """Validate that a value is a boolean."""
    if not isinstance(value, bool):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{field_name} must be a boolean."
        )

def check_plant_event_exists(session: Session, event_id: int):
    """Check if a PlantEvent with the given ID exists."""
    exists = session.execute(select(PlantEvent).where(PlantEvent.id == event_id)).scalar_one_or_none()
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"PlantEvent with ID {event_id} does not exist."
        )

def check_iot_dev_event_exists(session: Session, event_id: int):
    """Check if an IotDevEvent with the given ID exists."""
    exists = session.execute(select(IotDevEvent).where(IotDevEvent.id == event_id)).scalar_one_or_none()
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"IotDevEvent with ID {event_id} does not exist."
        )