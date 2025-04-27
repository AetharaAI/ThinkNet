from typing import List
from collections import Counter

class OutputWeighting:
    """
    Assigns dynamic weights to model outputs based on frequency and similarity.
    """

    def calculate_weights(self, responses: List[str]) -> List[float]:
        """
        Simple frequency-based weighting.
        """
        counter = Counter(responses)
        total = sum(counter.values())

        weights = [counter[resp] / total for resp in responses]
        return weights
