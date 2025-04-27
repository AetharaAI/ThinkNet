from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer, AutoModelForSeq2SeqLM
import random

app = FastAPI()

# 🚀 CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🚀 Load 3 Models
# 1. Creative Brain
creative_model_name = "distilgpt2"
creative_tokenizer = AutoTokenizer.from_pretrained(creative_model_name)
creative_model = AutoModelForCausalLM.from_pretrained(creative_model_name)
creative_generator = pipeline("text-generation", model=creative_model, tokenizer=creative_tokenizer)

# 2. Logical Technical Brain
logic_model_name = "EleutherAI/gpt-neo-125M"
logic_tokenizer = AutoTokenizer.from_pretrained(logic_model_name)
logic_model = AutoModelForCausalLM.from_pretrained(logic_model_name)
logic_generator = pipeline("text-generation", model=logic_model, tokenizer=logic_tokenizer)

# 3. Emotional Brain
emotional_model_name = "google/flan-t5-large"
emotional_tokenizer = AutoTokenizer.from_pretrained(emotional_model_name)
emotional_model = AutoModelForSeq2SeqLM.from_pretrained(emotional_model_name)
emotional_generator = pipeline("text2text-generation", model=emotional_model, tokenizer=emotional_tokenizer)

# 🚀 Prompt Input
class PromptRequest(BaseModel):
    prompt: str

# 🚀 Real /generate Route
@app.post("/generate")
async def generate_response(request: PromptRequest):
    prompt = request.prompt

    # Randomly pick one brain for now
    brain_choice = random.choice(["creative", "logic", "emotional"])

    if brain_choice == "creative":
        generated = creative_generator(prompt, max_length=150, num_return_sequences=1)
        response_text = generated[0]["generated_text"]
    elif brain_choice == "logic":
        generated = logic_generator(prompt, max_length=150, num_return_sequences=1)
        response_text = generated[0]["generated_text"]
    elif brain_choice == "emotional":
        generated = emotional_generator(prompt, max_length=150, num_return_sequences=1)
        response_text = generated[0]["generated_text"]

    return {"response": f"(Brain: {brain_choice}) {response_text}"}
