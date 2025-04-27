from core.base_model_interface import BaseModelInterface

class MockModel(BaseModelInterface):
    """
    Simple mock model for fast testing.
    """

    async def generate_response(self, prompt: str) -> str:
        return f"Mock response to: {prompt}"

    def get_specialty(self) -> str:
        return "mock"
