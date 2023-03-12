### **Icathia**

Icathia is an asynchronous Python wrapper library for [League Client API](https://developer.riotgames.com/docs/lol#game-client-api) that provides the possibility of sending any HTTP request to it.

### **Example of use**
* main.py

    ```python
    from icathia import Client

    import asyncio

    async def main():
        client = Client()

        try:
            await client.start()

            # If no summoner is found, it defaults to Dummy
            print(await client.get_summoner())
        finally:
            await client.close()

    if __name__ == "__main__":
        asyncio.run(main())
    ```

* Sending a request to retrieve current game phase of a League Client
    ```python
    response = await client.request("GET", "/lol-gameflow/v1/session")
    data = await response.json()
    if data.get("gameData") is not None:
        print(f"Game phase: {data.get('phase')}")
    else:
        print("Not in game")
    ```
    Output:
    ```
    Game phase: Lobby
    ```