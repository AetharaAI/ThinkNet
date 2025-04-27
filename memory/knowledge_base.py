class KnowledgeBase:
    """
    Basic shared knowledge across all models.
    Static for now, dynamic in future versions.
    """

    facts = {
        "python": "Python is a high-level, interpreted programming language.",
        "ai": "Artificial Intelligence is the simulation of human intelligence by machines.",
        "brain collective": "Brain Collective is a hive-mind architecture combining multiple LLMs."
    }

    @classmethod
    def get_fact(cls, topic: str) -> str:
        return cls.facts.get(topic.lower(), "No knowledge available on this topic.")

    @classmethod
    def add_fact(cls, topic: str, fact: str):
        cls.facts[topic.lower()] = fact
