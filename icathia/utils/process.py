from typing import AnyStr, ByteString

import asyncio
import re 

async def get_league_process_cmd() -> ByteString:
    process = await asyncio.subprocess.create_subprocess_shell(
        'wmic process where name="LeagueClientUx.exe" get commandline',
        stdout=asyncio.subprocess.PIPE)
    output, _ = await process.communicate()
    return output

def get_league_rmt_auth_token(string: AnyStr) -> str:
    if isinstance(string, str):
        string = string.encode()

    if (s := re.search(b'--remoting-auth-token=(.*?)"', string)) is not None:
        return s.group(1).decode()
    return ""

def get_league_port(string: AnyStr) -> int:
    if isinstance(string, str):
        string = string.encode()

    if (s := re.search(b"--app-port=(\d+)", string)) is not None:
        return int(s.group(1))
    return 0