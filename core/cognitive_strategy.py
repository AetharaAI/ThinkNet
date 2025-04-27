from typing import List
from collections import Counter
import random

class CognitiveStrategy:
    """
    Provides different strategies for combining model outputs intelligently.
    """

    @staticmethod
    def majority_vote(responses: List[str]) -> str:
        """
        Select the most frequent response among models.
        """
        if not responses:
            return ""
        
        count = Counter(responses)
        most_common = count.most_common(1)
        return most_common[0][0] if most_common else ""

    @staticmethod
    def weighted_choice(responses: List[str], weights: List[float]) -> str:
        """
        Select one response based on calculated weights.
        """
        if not responses or not weights:
            return ""

        total = sum(weights)
        normalized_weights = [w / total for w in weights]

        return random.choices(responses, weights=normalized_weights, k=1)[0]
