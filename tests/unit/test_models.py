import pytest
from tests.mocks.mock_models import MockModel

@pytest.mark.asyncio
async def test_mock_model_response():
    model = MockModel()
    response = await model.generate_response("test")
    assert "Mock response to" in response
