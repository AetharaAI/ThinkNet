from models.language_model import LanguageModel
from models.logic_model import LogicModel
from models.creative_model import CreativeModel
from models.technical_model import TechnicalModel
from models.emotional_model import EmotionalModel
# Add more models here as needed

from core.orchestrator import Orchestrator

class HiveMind:
    """
    Main class representing the collective intelligence of all models.
    Inherits capabilities dynamically from all specialized models.
    """

    def __init__(self):
        # Initialize specialized models
        self.models = [
            LanguageModel(),
            LogicModel(),
            CreativeModel(),
            TechnicalModel(),
            EmotionalModel()
            # Add more models
        ]

        # Initialize orchestrator
        self.orchestrator = Orchestrator(self.models)

    async def ask(self, prompt: str) -> str:
        """
        Public API to interact with the brain collective.
        """
        return await self.orchestrator.handle_prompt(prompt)
