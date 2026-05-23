from fastapi import APIRouter
from app.models.request_models import ChatRequest
from app.services.gemini_service import generate_response

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    response = generate_response(request.prompt)
    return {"response": response}

@router.get("/health")
async def health():
    return {"status": "ok"}

@router.get("/ready")
async def readiness():

    return {
        "status": "ready"
    }