from .summoner import Summoner
from .utils import process

from base64 import b64encode

import aiohttp

class Client(aiohttp.ClientSession):
    def __init__(self):
        super().__init__(connector=aiohttp.TCPConnector(verify_ssl=False))

        self.port: int = 0

        self.remote_auth_token: str = ""
        self.credentials: str = ""
        self.url: str = "https://127.0.0.1:{}"

        self.summoner: Summoner = None

    async def request(self, method, endpoint, **kwargs):
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = self.credentials

        return await super().request(method, f"{self.url}{endpoint}", headers=headers, **kwargs)

    async def start(self):
        cmd = await process.get_league_process_cmd()

        self.remote_auth_token = process.get_league_rmt_auth_token(cmd)
        self.port = process.get_league_port(cmd)

        if not self.remote_auth_token or not self.port:
            raise Exception("Either the remote authentication token or port field is invalid. "
                            "Try reopening League Client")
        
        encoded = b64encode(f"riot:{self.remote_auth_token}".encode())
        self.credentials = f"Basic {encoded.decode()}"
        self.url = self.url.format(self.port)

    async def get_summoner(self) -> Summoner:
        response = await self.request("GET", "/lol-summoner/v1/current-summoner")
        self.summoner = Summoner(**await response.json())
        return self.summoner