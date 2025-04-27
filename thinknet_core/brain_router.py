from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

# Brain server URLs (local microservices)
BRAIN_ENDPOINTS = {
    "emotionalmodel": "http://localhost:5001/generate",
    "technicalmodel": "http://localhost:5002/generate",
    "langaugemodel": "http://localhost:5003/generate",
    "logicmodel": "http://localhost:5004/generate",
    "creativemodel": "http://localhost:5005/generate",
}

# Prompt input schema
class PromptRequest(BaseModel):
    prompt: str

# Very Basic Intent Analyzer (expand later)
def choose_brain(prompt: str) -> str:
    prompt_lower = prompt.lower()

    if any(keyword in prompt_lower for keyword in ["feel", "emotions", "relationship", "happy", "sad", "love"]):
        return "emotionalmodel"
    elif any(keyword in prompt_lower for keyword in ["how", "why", "calculate", "prove", "analyze", "logic"]):
        return "logicmodel"
    elif any(keyword in prompt_lower for keyword in ["build", "design", "create", "imagine", "story", "art"]):
        return "creativemodel"
    elif any(keyword in prompt_lower for keyword in ["define", "describe", "language", "translate", "meaning"]):
        return "langaugemodel"
    elif any(keyword in prompt_lower for keyword in ["technology", "engineering", "program", "code", "system"]):
        return "technicalmodel"
    else:
        return random.choice(list(BRAIN_ENDPOINTS.keys()))  # fallback random

# Main /ask route
@app.post("/ask")
async def ask_thinknet(request: PromptRequest):
    chosen_brain = choose_brain(request.prompt)
    brain_url = BRAIN_ENDPOINTS.get(chosen_brain)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(brain_url, json={"prompt": request.prompt})
            data = response.json()
            return {
                "brain_used": chosen_brain,
                "response": data.get("response", "No response received.")
            }
        except Exception as e:
            return {"error": str(e)}

# Server boot
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
