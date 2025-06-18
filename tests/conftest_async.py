import pytest
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlmodel import SQLModel
from app.models import Basic  # 根據實際情況修改

TEST_DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/test_db"

engine = create_async_engine(TEST_DATABASE_URL, future=True, echo=True)
TestSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False, autoflush=False, autocommit=False)

@pytest.fixture(scope="module", autouse=True)
async def prepare_database():
    assert "test_db" in TEST_DATABASE_URL, "Test database URL must contain 'test_db'"
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

async def override_get_async_session():
    async with TestSessionLocal() as session:
        yield session