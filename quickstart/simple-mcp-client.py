import asyncio
from fastmcp import Client

client = Client("quickstart/simple-mcp-server.py")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("get_weather", {"location": "australia"})
        print(result)

asyncio.run(call_tool("Ford"))