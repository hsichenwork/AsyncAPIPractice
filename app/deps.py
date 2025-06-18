from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import async_session
from app.core.syncDb import SyncSessionLocal

async def get_async_session():
    async with async_session() as session:
        yield session

SessionDep = Annotated[AsyncSession, Depends(get_async_session)]

def get_sync_session():
    with SyncSessionLocal() as session:
        yield session

SyncSessionDep = Annotated[Session, Depends(get_sync_session)]
