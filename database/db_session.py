from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from utils.config_loader import ConfigLoader

# Load DB config
config = ConfigLoader.load_config('config/db_config.yaml')
DATABASE_URL = config['database_url']

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
