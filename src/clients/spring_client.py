import httpx
from src.core.config import Config

class SpringClient:
    def __init__(self):
        self.base_url = Config.SPRING_BOOT_URL

    async def fetch_user_profile(self, user_id: int) -> dict:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{self.base_url}/api/v1/users/{user_id}/profile")
            resp.raise_for_status()
            return resp.json()

spring_client = SpringClient()