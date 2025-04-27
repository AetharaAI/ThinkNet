from typing import List
from core.base_model_interface import BaseModelInterface
from integration.consensus_builder import ConsensusBuilder
from memory.short_term_memory import ShortTermMemory
from core.task_router import TaskRouter

class Orchestrator:
    """
    Orchestrates the flow from input -> task routing -> model responses -> consensus.
    """

    def __init__(self, models: List[BaseModelInterface]):
        self.models = models
        self.task_router = TaskRouter(models)
        self.consensus_builder = ConsensusBuilder()
        self.memory = ShortTermMemory()

    async def handle_prompt(self, prompt: str) -> str:
        # Save incoming prompt into short term memory
        self.memory.store_prompt(prompt)

        # Route prompt to relevant models
        selected_models = self.task_router.route(prompt)

        if not selected_models:
            raise ValueError("No available models to handle the prompt.")

        # Gather responses asynchronously
        responses = await self._gather_responses(selected_models, prompt)

        # Build a consensus response
        final_response = self.consensus_builder.build(responses)

        # Save final response to memory
        self.memory.store_response(final_response)

        return final_response

    async def _gather_responses(self, models: List[BaseModelInterface], prompt: str) -> List[str]:
        results = []
        for model in models:
            try:
                response = await model.generate_response(prompt)
                results.append(response)
            except Exception as e:
                print(f"[Error] {model.get_specialty()} model failed: {e}")
        return results
