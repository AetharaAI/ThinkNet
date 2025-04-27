from fastapi import APIRouter, HTTPException
from api.schema import PromptRequest, PromptResponse
from core.hive_mind import HiveMind

router = APIRouter()
hive_mind = HiveMind()

@router.post("/ask", response_model=PromptResponse)
async def ask_hive(prompt_request: PromptRequest):
    try:
        response = await hive_mind.ask(prompt_request.prompt)
        return PromptResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in HiveMind: {e}")
