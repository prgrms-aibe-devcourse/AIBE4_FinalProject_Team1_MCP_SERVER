from fastmcp import FastMCP
from src.clients.spring_client import spring_client

mcp = FastMCP()

@mcp.tool()
async def get_user_profile(user_id: int) -> dict:
    """
    사용자의 프로필 정보를 조회합니다. 
    이름, 이메일의 정보를 포함합니다.
    """
    return await spring_client.fetch_user_profile(user_id)