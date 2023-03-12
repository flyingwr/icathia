class Summoner:
    def __init__(self, **kwargs):
        self.id: int = kwargs.get("accountId", 0)
        self.uuid: str = kwargs.get("puuid")

        self.internal_name: str = kwargs.get("internalName", "Dummy")
        self.name: str = kwargs.get("displayName", "Dummy")

        self.profile_icon_id: int = kwargs.get("profileIconId", 0)
        self.level: int = kwargs.get("summonerLevel", 0)

    def __repr__(self) -> str:
        return f"Summoner `{self.name}`"