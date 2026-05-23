from fastapi.responses import JSONResponse
from google.genai.errors import ClientError

async def global_exception_handler(request, exc):

    if isinstance(exc, ClientError):
        return JSONResponse(
            status_code=exc.code if exc.code else 420,
            content={
                "status": "error",
                "message": "Gemini API Quota or Client limit reached.",
                "details": exc.message
            }
        )
        
    # Fallback for any other unexpected backend crashes
    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "An unexpected internal server error occurred.",
            "details": str(exc)
        }
    )