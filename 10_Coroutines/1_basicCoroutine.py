async def greet(name):
    return f"Hello, {name}!"

async def main():
    result = await greet("Alice")
    print(result)

import asyncio
asyncio.run(main())
