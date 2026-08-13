'''import asyncio

async def hello(user:str):
    print(f"hello{user}")
    await asyncio.sleep(0)
    print(f"hello{user}")
asyncio.run(hello("kumaran"))'''

import asyncio

async def gather(name:str,delay:int):
    print(f"")
