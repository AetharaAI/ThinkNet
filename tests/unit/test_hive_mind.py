import pytest
from core.hive_mind import HiveMind

@pytest.mark.asyncio
async def test_hive_ask():
    hive = HiveMind()
    response = await hive.ask("test input")
    assert isinstance(response, str)
