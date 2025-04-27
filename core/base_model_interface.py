from abc import ABC, abstractmethod

class BaseModelInterface(ABC):
    """
    Abstract Base Class defining a unified interface for all specialized models.
    Each model must implement the generate_response method.
    """

    @abstractmethod
    async def generate_response(self, prompt: str) -> str:
        """
        Generate a model-specific response to the given prompt.
        """
        pass

    @abstractmethod
    def get_specialty(self) -> str:
        """
        Return the cognitive specialty of the model (e.g., 'logic', 'creativity').
        """
        pass
