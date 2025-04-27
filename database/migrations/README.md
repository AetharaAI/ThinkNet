# Database Migrations

You can use Alembic or SQLAlchemy Core to manage migrations.

Example to create DB:

```bash
python
>>> from database.models import Base
>>> from database.db_session import engine
>>> async def init_db():
>>>     async with engine.begin() as conn:
>>>         await conn.run_sync(Base.metadata.create_all)

>>> import asyncio
>>> asyncio.run(init_db())
