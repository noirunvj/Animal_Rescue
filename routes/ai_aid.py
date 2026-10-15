from fastapi import APIRouter, HTTPException
from schemas import AIAidRequest

router = APIRouter(prefix="/api/ai", tags=["AI First-Aid"])

@router.post("/first-aid")
async def get_first_aid(data: AIAidRequest):
    try:
        return {
            "success": True,
            "injury_reported": data.injury_description,
            "stabilization_steps": [
                "1. Keep the animal calm and avoid sudden physical contact.",
                "2. If bleeding profusely, apply gentle direct pressure with a clean cloth.",
                "3. Keep airways unobstructed; do not force water or food if the animal is semi-conscious."
            ],
            "disclaimer": "Emergency stabilization only. Transfer to a licensed veterinarian immediately."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
