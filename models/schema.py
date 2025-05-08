from sqlalchemy import Column, Integer, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class Log(Base):
    __tablename__ = "Log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    entry_creation_time = Column(DateTime, nullable=False)
    entry_store_time = Column(DateTime, default=datetime.now(timezone.utc))

    temperature = Column(Float, nullable=False)
    luminosity_state = Column(Float, nullable=False)
    humidity_state = Column(Float, nullable=False)
    luminosity_event = Column(Float, nullable=False)
    humidity_event = Column(Float, nullable=False)

    plant_id = Column(Integer, ForeignKey("Plant.id"), nullable=False)
    plant = relationship("Plant", back_populates="logs")

    valve_state = Column(Boolean, nullable=False)
    pump_state = Column(Boolean, nullable=False)
    led_intensity_state = Column(Integer, nullable=False)

    valve_event = Column(Boolean, nullable=False)
    pump_event = Column(Boolean, nullable=False)
    led_intensity_event = Column(Integer, nullable=False)
    
    mode_event = Column(Integer, nullable=False, default=0)
    mode_state = Column(Integer, nullable=False, default=0)

class PlantState(Base):
    __tablename__ = "PlantState"

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_updated = Column(DateTime, default=datetime.now(timezone.utc))

    luminosity_state = Column(Float, nullable=False)
    humidity_state = Column(Float, nullable=False)

    valve_state = Column(Boolean, nullable=False)
    led_intensity_state = Column(Integer, nullable=False)
    
    mode = Column(Integer, nullable=False, default=0)

    plants = relationship("Plant", back_populates="plant_state", primaryjoin="PlantState.id==Plant.plant_state_id", foreign_keys="[Plant.plant_state_id]")


class PlantEvent(Base):
    __tablename__ = "PlantEvent"

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_updated = Column(DateTime, default=datetime.now(timezone.utc))

    luminosity_event = Column(Float, nullable=False)
    humidity_event = Column(Float, nullable=False)

    valve_event = Column(Boolean, nullable=False)
    led_intensity_event = Column(Integer, nullable=False)
    
    mode = Column(Integer, nullable=False, default=0)

    plants = relationship("Plant",back_populates="plant_event",primaryjoin="PlantEvent.id==Plant.plant_event_id",foreign_keys="[Plant.plant_event_id]")


class Plant(Base):
    __tablename__ = "Plant"

    id = Column(Integer, primary_key=True, autoincrement=True)
    error = Column(Boolean, nullable=False)

    plant_state_id = Column(Integer, ForeignKey("PlantState.id"), nullable=False)
    plant_event_id = Column(Integer, ForeignKey("PlantEvent.id"), nullable=False)
    iot_dev_id = Column(Integer, ForeignKey("IotDev.id"), nullable=False)

    plant_state = relationship("PlantState", back_populates="plants")
    plant_event = relationship("PlantEvent", back_populates="plants")
    iot_dev = relationship("IotDev", back_populates="plants")

    logs = relationship("Log", back_populates="plant")


class IotDev(Base):
    __tablename__ = "IotDev"

    id = Column(Integer, primary_key=True, autoincrement=True)
    online_status = Column(Boolean, nullable=False)
    dev_state_id = Column(Integer, ForeignKey("IotDevState.id"), nullable=False)
    dev_event_id = Column(Integer, ForeignKey("IotDevEvent.id"), nullable=False)

    dev_state = relationship("IotDevState", back_populates="iot_devs")
    dev_event = relationship("IotDevEvent", back_populates="iot_devs")

    plants = relationship("Plant", back_populates="iot_dev")


class IotDevState(Base):
    __tablename__ = "IotDevState"

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_updated = Column(DateTime, default=datetime.now(timezone.utc))
    pump_state = Column(Boolean, nullable=False)

    iot_devs = relationship("IotDev", back_populates="dev_state")


class IotDevEvent(Base):
    __tablename__ = "IotDevEvent"

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_updated = Column(DateTime, default=datetime.now(timezone.utc))
    pump_event = Column(Boolean, nullable=False)

    iot_devs = relationship("IotDev", back_populates="dev_event")