class ShortTermMemory:
    """
    Short-Term Memory for session-based storage.
    Keeps track of prompts and responses temporarily.
    """

    def __init__(self):
        self.prompts = []
        self.responses = []

    def store_prompt(self, prompt: str):
        self.prompts.append(prompt)

    def store_response(self, response: str):
        self.responses.append(response)

    def recall(self) -> dict:
        """
        Recall the last interaction.
        """
        if self.prompts and self.responses:
            return {"prompt": self.prompts[-1], "response": self.responses[-1]}
        return {"prompt": None, "response": None}

    def clear(self):
        """
        Clear the session memory.
        """
        self.prompts.clear()
        self.responses.clear()
