from fastmcp import FastMCP
import asyncio

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Gets the weather given a location
    Args:
        location: location, can be city, country, state, etc.
    """
    return "The weather is hot and dry"


if __name__== "__main__":
    asyncio.run(mcp.run())