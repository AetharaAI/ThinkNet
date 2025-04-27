from core.base_model_interface import BaseModelInterface
import httpx

class CreativeModel(BaseModelInterface):
    """
    Creative Specialist Model - Handles idea generation, storytelling, design prompts.
    """

    def __init__(self):
        self.api_url = "http://localhost:5003/generate"

    async def generate_response(self, prompt: str) -> str:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.api_url, json={"prompt": prompt})
                response.raise_for_status()
                return response.json().get("response", "Creative model failed to return output.")
        except Exception as e:
            return f"[CreativeModel Error]: {e}"

    def get_specialty(self) -> str:
        return "creativity"
