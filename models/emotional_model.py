from core.base_model_interface import BaseModelInterface
import httpx

class EmotionalModel(BaseModelInterface):
    """
    Emotional Specialist Model - Handles empathy, emotional tone analysis, counseling.
    """

    def __init__(self):
        self.api_url = "http://localhost:5005/generate"

    async def generate_response(self, prompt: str) -> str:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.api_url, json={"prompt": prompt})
                response.raise_for_status()
                return response.json().get("response", "Emotional model failed to return output.")
        except Exception as e:
            return f"[EmotionalModel Error]: {e}"

    def get_specialty(self) -> str:
        return "emotional"
