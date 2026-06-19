from fastapi import FastAPI
from app.routes import scam

app = FastAPI(
    title="ScamShield API",
    description="API for detecting scam messages and eexplaining red flags.",
    version="1.0.0",
)

app.include_router(scam.router, prefix="/api", tags=["Scam Analysis"])

@app.get("/")
def root():
    return {"message": "ScamShield API is running "}