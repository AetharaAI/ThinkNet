from core.hive_mind import HiveMind
from web.app import create_app
import uvicorn

# Initialize Hive Mind Core
hive_mind = HiveMind()

# Create FastAPI app
app = create_app(hive_mind)

if __name__ == "__main__":
    uvicorn.run("run_brain_collective:app", host="0.0.0.0", port=8000, reload=True)
