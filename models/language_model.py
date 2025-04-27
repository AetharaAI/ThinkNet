from core.base_model_interface import BaseModelInterface
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch

class LanguageModel(BaseModelInterface):
    """
    Language Specialist Model
    Loads and runs a text generation model (e.g., distilgpt2) directly using transformers.
    """

    def __init__(self):
        model_name = "distilgpt2"
        self.device = 0 if torch.cuda.is_available() else -1

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

        self.generator = pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=self.device
        )

    async def generate_response(self, prompt: str) -> str:
        """
        Generates a response locally without any API calls.
        """
        try:
            output = self.generator(prompt, max_length=100, do_sample=True)
            return output[0]['generated_text']
        except Exception as e:
            return f"[LanguageModel Error]: {e}"

    def get_specialty(self) -> str:
        return "language"
