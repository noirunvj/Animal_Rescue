from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class IncidentModel(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    animal_type = Column(String, nullable=False)
    injury_description = Column(String, nullable=False)
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
