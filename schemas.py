from pydantic import BaseModel

class EmergencyRequest(BaseModel):
    latitude: float
    longitude: float
    animal_type: str
    injury_description: str

class RoutineRequest(BaseModel):
    location_name: str
    pet_type: str
    condition: str

class AIAidRequest(BaseModel):
    injury_description: str
