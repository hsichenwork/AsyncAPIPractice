from fastapi import FastAPI, status
from contextlib import asynccontextmanager
from app.models import Basic
from app.crud import create_todo, get_todos, get_sync_todos
from app.core.db import init_db
from app.deps import SessionDep, SyncSessionDep


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/", status_code=status.HTTP_200_OK)
async def read_root() -> dict:
    return {"message": "Hello World"}

@app.post("/todos", status_code=status.HTTP_201_CREATED)
async def add_todo(db: SessionDep, todo: Basic) -> Basic:
    return await create_todo(db,todo.name, todo.job)

@app.get("/todos", status_code=status.HTTP_200_OK)
async def list_todos(db: SessionDep) -> list[Basic]:
    return await get_todos(db)

@app.get("/sync-todos", status_code=status.HTTP_200_OK)
def list_sync_todos(db: SyncSessionDep) -> list[Basic]:
    return get_sync_todos(db)