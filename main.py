from icathia import Client

import asyncio

async def main():
    client = Client()

    try:
        await client.start()
        print(await client.get_summoner()) # If no summoner is found, it defaults to Dummy
    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())