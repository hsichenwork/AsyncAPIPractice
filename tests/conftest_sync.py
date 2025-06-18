import pytest
from sqlmodel import create_engine, SQLModel, Session
from sqlalchemy.orm import sessionmaker

TEST_DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/test_db"
engine = create_engine(TEST_DATABASE_URL, echo=True)
TestSyncSessionDb = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)

@pytest.fixture(scope="module", autouse=True)
def setup_test_database():
    assert "test_db" in str(engine.url), "不應該使用正式資料庫進行測試！"
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)

def override_get_db_session():
    with TestSyncSessionDb() as session:
        yield session