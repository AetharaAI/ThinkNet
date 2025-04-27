from typing import List
from integration.output_weighting import OutputWeighting
from integration.conflict_resolution import ConflictResolution
from core.cognitive_strategy import CognitiveStrategy

class ConsensusBuilder:
    """
    Builds a unified response by merging model outputs through dynamic strategies.
    """

    def __init__(self):
        self.output_weighting = OutputWeighting()
        self.conflict_resolution = ConflictResolution()

    def build(self, responses: List[str]) -> str:
        """
        Main method to create a consensus from multiple model responses.
        """
        if not responses:
            return "No responses available."

        # Calculate weights
        weights = self.output_weighting.calculate_weights(responses)

        # Attempt majority vote first
        voted_response = CognitiveStrategy.majority_vote(responses)

        if not voted_response:
            # Fall back to weighted choice if no clear majority
            final_response = CognitiveStrategy.weighted_choice(responses, weights)
        else:
            final_response = voted_response

        # Conflict resolution (basic for now)
        final_response = self.conflict_resolution.resolve(final_response)

        return final_response
