from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import EmergencyRequest
from database import get_db
from models import IncidentModel
from tinyfish import AsyncTinyFish
from config import TINYFISH_API_KEY

router = APIRouter(prefix="/api/emergency", tags=["Emergency Operations"])
tinyfish_client = AsyncTinyFish(api_key=TINYFISH_API_KEY)

@router.post("/broadcast")
async def broadcast_emergency(data: EmergencyRequest, db: Session = Depends(get_db)):
    try:
        new_incident = IncidentModel(
            latitude=data.latitude,
            longitude=data.longitude,
            animal_type=data.animal_type,
            injury_description=data.injury_description
        )
        db.add(new_incident)
        db.commit()
        db.refresh(new_incident)

        goal_text = f"Find 24/7 emergency veterinary clinics, phone numbers, and addresses near coordinates {data.latitude}, {data.longitude}"
        agent_response = await tinyfish_client.agent.run(
            goal=goal_text,
            url="https://www.google.com/maps"
        )

        return {
            "success": True,
            "message": "Emergency broadcast logged to PostgreSQL and TinyFish search executed.",
            "incident_id": new_incident.id,
            "live_vets_scraped": agent_response
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
