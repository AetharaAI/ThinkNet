import pytest
from core.orchestrator import Orchestrator
from tests.mocks.mock_models import MockModel

@pytest.mark.asyncio
async def test_orchestrator_basic():
    models = [MockModel()]
    orchestrator = Orchestrator(models)
    result = await orchestrator.handle_prompt("test prompt")
    assert "Mock response to" in result
