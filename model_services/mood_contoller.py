from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yaml
import os

app = FastAPI()

MODELS_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "models_config.yaml")

class MoodChangeRequest(BaseModel):
    role: str
    new_bias: str

@app.post("/change_mood")
async def change_mood(request: MoodChangeRequest):
    try:
        with open(MODELS_CONFIG_PATH, "r") as f:
            config = yaml.safe_load(f)

        if request.role not in config:
            raise HTTPException(status_code=404, detail=f"Role '{request.role}' not found in config.")

        config[request.role]["bias_direction"] = request.new_bias

        with open(MODELS_CONFIG_PATH, "w") as f:
            yaml.dump(config, f)

        return {"message": f"Bias for {request.role} updated to '{request.new_bias}' successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
