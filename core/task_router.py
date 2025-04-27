from typing import List
from core.base_model_interface import BaseModelInterface

class TaskRouter:
    """
    Routes tasks to the most appropriate specialized models based on prompt analysis.
    """

    def __init__(self, models: List[BaseModelInterface]):
        self.models = models

    def route(self, prompt: str) -> List[BaseModelInterface]:
        """
        Basic keyword-based task routing.
        """
        selected = []
        prompt_lower = prompt.lower()

        for model in self.models:
            specialty = model.get_specialty().lower()
            if specialty in prompt_lower:
                selected.append(model)

        # Fallback: if no matches, use all models
        if not selected:
            return self.models
        
        return selected
