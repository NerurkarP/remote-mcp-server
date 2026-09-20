
import json
import random
from fastmcp import FastMCP

mcp = FastMCP("Demo Server")

@mcp.tool()
def roll_dice(n_dice: int = 1) -> list[int]:
    "Roll n_dice 6 sided dice  and return the result"
    return [random.randint(1,6) for _ in range(n_dice)]

@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    "Add 2 numbers together"
    return a+b

@mcp.resource("info://server")
def get_server_info() -> str:
    '''Get info about this server'''
    info= {
        "name":"Simple Calculator server",
        "version":"1.0",
        "description":"A basic remote mcp server with Math tools",
        "tools": ["add_number", "roll_dice"],
        "author":"ABC Inc"     
    }
    return json.dumps(info,indent=2)
    

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)