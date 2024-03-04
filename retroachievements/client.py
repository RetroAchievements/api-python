import requests as request
from retroachievements import __version__


class RAClient:
    """
    Main class for accessing the RetroAhievements Web API
    """

    headers = {
        "User-Agent": "RetroAchievements-api-python/" + __version__}

    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

    def url_params(self, params=None):
        """
        Inserts the auth and query params into the request
        """
        if params is None:
            params = {}
        params.update({"z": self.username, "y": self.api_key})
        return params

    # URL construction
    def _call_api(self, endpoint=None, params=None, timeout=30, headers=None):
        if endpoint is None:
            endpoint = {}
        req = request.get(
            f"https://retroachievements.org/API/{endpoint}",
            params=self.url_params(params),
            timeout=timeout,
            headers=headers,
        )
        return req

    # User endpoints

    def GetUserPoints(self, user: str) -> dict:
        """
        Get a user's total hardcore and softcore points

        Params:
            u: Username to query
        """
        result = self._call_api("API_GetUserPoints.php?", {"u": user}).json()
        return result

    def GetUserSummary(self, user: str, recent_games=0, recent_cheevos=10) -> dict:
        """
        Get a user's exhaustive profile metadata

        Params:
            u: Username to query
            g: Number of recent games to fetch, default = 0
            a: Number of recent achievements to fetch, default = 10
        """
        result = self._call_api(
            "API_GetUserSummary.php?",
            {"u": user, "g": recent_games, "a": recent_cheevos},
        ).json()
        return result

    # Game endpoints

    def GetGame(self, game: int) -> dict:
        """
        Get basic metadata about a game

        Params:
            i: The game ID to query
        """
        result = self._call_api("API_GetGame.php?", {"i": game}).json()
        return result

    def GetGameExtended(self, game: int) -> dict:
        """
        Get extended metadata about a game

        Params:
            i: The game ID to query
        """
        result = self._call_api("API_GetGameExtended.php?", {"i": game}).json()
        return result

    def GetAchievementCount(self, game: int) -> dict:
        """
        Get the list of achievement ID's for a game

        Params:
            i: The game ID to query
        """
        result = self._call_api(
            "API_GetAchievementCount.php?", {"i": game}).json()
        return result

    def GetAchievementDistribution(self, game: int) -> dict:
        """
        Get how many players have unlocked how many achievements for a game

        Params:
            i: The game ID to query
        """
        result = self._call_api(
            "API_GetAchievementDistribution.php?", {"i": game}
        ).json()
        return result

    # System Endpoints

    def GetConsoleIds(self) -> list:
        """
        Get the complete list of console ID and name pairs on the site

        Params:
            None
        """
        result = self._call_api("API_GetConsoleIDs.php?", {None}).json()
        return result

    def GetGameList(self, system: int, has_cheevos=0, hashes=0) -> dict:
        """
        Get the complete list of games for a console

        Params:
            i: The system ID to query
            f: If 1, only returns games that have achievements (default = 0)
            h: If 1, also return the supported hashes for games (default = 0)
        """
        result = self._call_api(
            "API_GetGameList.php?", {
                "i": system, "f": has_cheevos, "h": hashes}
        ).json()
        return result
