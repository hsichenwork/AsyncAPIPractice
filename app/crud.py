from sqlmodel import select
from app.models import Basic
import time
import asyncio

async def create_todo(db, name: str, job: str) -> Basic:
    todo = Basic(name=name, job=job)
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo

async def get_todos(db) -> list[Basic]:
    result = await db.execute(select(Basic))
    return list(result.scalars().all())

def get_sync_todos(db) -> list[Basic]:
    result = db.execute(select(Basic))
    return list(result.scalars().all())