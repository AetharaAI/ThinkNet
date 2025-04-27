import sys
import os

from utils.config_loader import load_yaml_config

# --- FIXED relative import
from model_servers.memory.MemoryManager import MemoryManager


from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import torch
import yaml
from fastapi.middleware.cors import CORSMiddleware

# Load Config
def load_config(role):
    config_path = os.path.join(os.path.dirname(__file__), "models_config.yaml")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config.get(role, {})

# FastAPI app
app = FastAPI()

# CORS (frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Read brain ROLE from command-line
ROLE = sys.argv[1]

# --- Load Model Settings
config = load_config(ROLE)

model_name = config.get("model_name", "distilgpt2")
temperature = config.get("temperature", 0.7)
top_p = config.get("top_p", 0.9)
repetition_penalty = config.get("repetition_penalty", 1.0)
max_length = config.get("max_length", 150)
bias_direction = config.get("bias_direction", "balanced, explanatory")

device = 0 if torch.cuda.is_available() else -1

# --- Load the Model
def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer, device=device)

generator = load_model(model_name)

# --- Memory Manager Setup
memory_manager = MemoryManager()

# --- Prompt Schema
class PromptRequest(BaseModel):
    prompt: str

# --- /generate Endpoint
@app.post("/generate")
async def generate_text(request: PromptRequest):
    memories = memory_manager.search_memory(request.prompt)

    if memories:
        memory_context = " ".join(memories)
        user_prompt = f"Use this context: {memory_context}\nUser asked: {request.prompt}"
    else:
        user_prompt = request.prompt

    full_prompt = f"You should respond in a {bias_direction} manner. {user_prompt}"

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

# --- /learn Endpoint
@app.post("/learn")
async def learn_memory(request: PromptRequest):
    memory_manager.add_memory(request.prompt)
    return {"message": "New memory stored successfully."}

# --- Run Server
if __name__ == "__main__":
    ports = {
        "emotionalmodel": 5001,
        "technicalmodel": 5002,
        "langaugemodel": 5003,
        "logicmodel": 5004,
        "creativemodel": 5005
    }
    port = ports.get(ROLE, 5001)

    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
