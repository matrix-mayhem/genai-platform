import google.genai as genai
from tenacity import retry, stop_after_attempt, wait_exponential
from app.utils.logger import logger
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

@retry(
    stop = stop_after_attempt(3),
    wait = wait_exponential(multiplier=1, min=2, max=10)
)
def generate_response(prompt: str) -> str:
    try:
        logger.info(f"Sending prompt to Gemini API: {prompt}")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        logger.info("REceived successful response from Gemini API")

        return response.text
    
    except Exception as e:
        logger.error(f"Gemini API request failed: {str(e)}")
        raise