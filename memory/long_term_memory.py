from database.db_session import get_db
from database.models import MemoryEntry
from sqlalchemy.future import select
import asyncio

class LongTermMemory:
    """
    Long-Term Memory for persistent storage across sessions.
    Uses the database backend.
    """

    async def store(self, prompt: str, response: str):
        async with get_db() as session:
            entry = MemoryEntry(prompt=prompt, response=response)
            session.add(entry)
            await session.commit()

    async def recall(self, limit: int = 10) -> list:
        async with get_db() as session:
            result = await session.execute(select(MemoryEntry).order_by(MemoryEntry.timestamp.desc()).limit(limit))
            return result.scalars().all()
