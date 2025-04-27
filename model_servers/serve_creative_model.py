from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch
import yaml
import os

# --- NEW import for memory
from model_services.memory.MemoryManager import MemoryManager

app = FastAPI()

ROLE = "creativemodel"  # << Set your role name per brain here

def load_config(role):
    config_path = os.path.join(os.path.dirname(__file__), "models_config.yaml")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config.get(role, {})

config = load_config(ROLE)

model_name = config.get("model_name", "distilgpt2")
temperature = config.get("temperature", 0.7)
top_p = config.get("top_p", 0.9)
repetition_penalty = config.get("repetition_penalty", 1.0)
max_length = config.get("max_length", 150)
bias_direction = config.get("bias_direction", "")

device = 0 if torch.cuda.is_available() else -1

# --- Cleaner model loading
def load_model_and_tokenizer(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=device)

generator = load_model_and_tokenizer(model_name)

# --- Memory manager setup
memory_manager = MemoryManager()

class PromptRequest(BaseModel):
    prompt: str

# --- Updated /generate
@app.post("/generate")
async def generate_text(request: PromptRequest):
    # Search memory before generation
    memories = memory_manager.search_memory(request.prompt)

    if memories:
        memory_context = " ".join(memories)
        user_prompt = f"Use this context to answer: {memory_context}\nUser asked: {request.prompt}"
    else:
        user_prompt = request.prompt

    # --- Bias Injection
    system_prompt = f"You should respond in a {bias_direction} manner. "
    full_prompt = system_prompt + user_prompt

    output = generator(
        full_prompt,
        max_length=max_length,
        temperature=temperature,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        num_return_sequences=1
    )
    return {"response": output[0]['generated_text']}

# --- New /learn endpoint
@app.post("/learn")
async def learn_memory(request: PromptRequest):
    memory_manager.add_memory(request.prompt)
    return {"message": "New memory stored successfully."}
