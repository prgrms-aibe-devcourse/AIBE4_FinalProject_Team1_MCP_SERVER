from src.mcp.tools import mcp
from src.core.config import Config

if __name__ == "__main__":
    mcp.run(
        transport="sse",
        host="0.0.0.0",
        port=Config.PORT,
    )