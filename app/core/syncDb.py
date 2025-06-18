from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, create_engine
from app.core.config import settings

DATABASE_URL = str(settings.SQLALCHEMY_SYNC_DATABASE_URI())
sync_engine = create_engine(DATABASE_URL)
SyncSessionLocal = sessionmaker(sync_engine, class_=Session, expire_on_commit=False)