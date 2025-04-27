from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from api.endpoints import router as api_router

templates = Jinja2Templates(directory="web/templates")

def create_app(hive_mind):
    app = FastAPI(title="Brain Collective - Hive Mind AI")

    app.include_router(api_router, prefix="/api")

    @app.get("/", response_class=HTMLResponse)
    async def home(request: Request):
        return templates.TemplateResponse("index.html", {"request": request})

    @app.post("/ask", response_class=HTMLResponse)
    async def ask(request: Request, user_prompt: str = Form(...)):
        from core.hive_mind import HiveMind
        hive = HiveMind()
        response = await hive.ask(user_prompt)
        return templates.TemplateResponse("index.html", {"request": request, "response": response, "prompt": user_prompt})

    return app
