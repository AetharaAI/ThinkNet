import pytest
from run_brain_collective import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_root_webpage():
    response = client.get("/")
    assert response.status_code == 200
    assert "Ask the Brain Collective" in response.text

@pytest.mark.asyncio
async def test_api_ask():
    payload = {"prompt": "Test prompt"}
    response = client.post("/api/ask", json=payload)
    assert response.status_code == 200
    assert "response" in response.json()
