import pytest
from httpx import AsyncClient
from httpx._transports.asgi import ASGITransport  # ✅ 重點：使用 ASGITransport
from app.main import app
from app.deps import get_async_session, get_sync_session
from conftest_async import override_get_async_session

transport = ASGITransport(app=app)

app.dependency_overrides[get_async_session] = override_get_async_session


class TestMain():
    @pytest.mark.asyncio
    async def test_read_root(self):
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}  # 根據實際修改

