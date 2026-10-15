from fastapi import APIRouter, HTTPException
from schemas import RoutineRequest

router = APIRouter(prefix="/api/routine", tags=["Routine Allocation"])

@router.post("/allocate")
async def allocate_vet_or_ngo(data: RoutineRequest):
    try:
        return {
            "success": True,
            "query": data.dict(),
            "allocated_facilities": [
                {
                    "name": "Community Animal Care Centre",
                    "type": "NGO Clinic",
                    "contact": "+91-9876543210",
                    "status": "Open",
                    "location": data.location_name
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
