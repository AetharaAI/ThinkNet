from core.base_model_interface import BaseModelInterface
import httpx

class LogicModel(BaseModelInterface):
    """
    Logic Specialist Model - Handles problem solving, critical reasoning, math.
    """

    def __init__(self):
        self.api_url = "http://localhost:5002/generate"

    async def generate_response(self, prompt: str) -> str:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.api_url, json={"prompt": prompt})
                response.raise_for_status()
                return response.json().get("response", "Logic model failed to return output.")
        except Exception as e:
            return f"[LogicModel Error]: {e}"

    def get_specialty(self) -> str:
        return "logic"
