from fastapi import FastAPI
from routes import emergency, routine, ai_aid
from database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Emergency Animal Response & Triage API",
    description="Full-stack backend powered by FastAPI, PostgreSQL, and TinyFish web agents.",
    version="1.0.0"
)

app.include_router(emergency.router)
app.include_router(routine.router)
app.include_router(ai_aid.router)

@app.get("/")
def root():
    return {"status": "online", "message": "Backend server is running successfully!"}
