
---

### 📄 `database/seeds.py`
```python
from database.models import MemoryEntry
from database.db_session import get_db

async def seed_database():
    """
    Seed initial knowledge or memory entries if needed.
    """
    sample_data = [
        MemoryEntry(prompt="What is AI?", response="AI stands for Artificial Intelligence."),
        MemoryEntry(prompt="Who invented Python?", response="Guido van Rossum created Python.")
    ]

    async with get_db() as session:
        for entry in sample_data:
            session.add(entry)
        await session.commit()
