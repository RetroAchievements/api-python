import requests as request
from retroachievements import __version__


_BASE_URL = "https://retroachievements.org/API/"


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
            f"{_BASE_URL}{endpoint}",
            params=self.url_params(params),
            timeout=timeout,
            headers=headers,
        )
        return req

    # User endpoints

    def get_user_points(self, user: str) -> dict:
        """
        Get a user's total hardcore and softcore points

        Params:
            u: Username to query
        """
        result = self._call_api("API_GetUserPoints.php?", {"u": user}).json()
        return result

    def get_user_summary(self, user: str,
                         recent_games=0,
                         recent_cheevos=10) -> dict:
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


    def get_recent_achievements(self, user: str) -> dict:
        """
        Get a user's most recent achievement within the last hour

        Params:
            u: Username to query
        """
        result = self._call_api("API_GetUserRecentAchievements.php?", {"u": user}).json()
        return result

    def get_game_progress(self, user: str, game: int) -> dict:
        """
        Get a users recent game info and progress

        Params:
            g: Game ID 
            u: Username to query
        """
        result = self._call_api("API_GetGameInfoAndUserProgress.php?", {"g": game, "u": user}).json()
        return result


    def get_achievements_on_day(self, user: str, date: int) -> dict:
        """
        Get a user's cheevos from a specific date

        Params:
            u: Username to query
            d: Date to query
        """
        result = self._call_api("API_GetAchievementsEarnedOnDay.php?", {"u": user, "d": date}).json()
        return result

    def get_achievements_range(self, user: str, f: int, t: int) -> dict:
        """
        Get a user's cheevos from a specific date

        Params:
            u: Username to query
            f: From date to query (must be in epoch timestamp format)
            t: To date to query (must be in epoch timestamp format)
        """
        result = self._call_api("API_GetAchievementsEarnedOnDay.php?", {"u": user, "f": f, "t": t }).json()
        return result

    def get_all_completion_progress(self, user: str) -> dict:
        """
        Get a user's info and progress on all games

        Params:
            u: Username to query
        """
        result = self._call_api("API_GetUserCompletionProgress.php?", {"u": user}).json()
        return result

    def get_awards_badges(self, user: str) -> list:
        """
        Get a user's awards and badges on RA

        Params:
            u: Username to query
        """
        result = self._call_api("API_GetUserAwards.php?", {"u": user}).json()
        return result
 

    # Game endpoints

    def get_game(self, game: int) -> dict:
        """
        Get basic metadata about a game

        Params:
            i: The game ID to query
        """
        result = self._call_api("API_GetGame.php?", {"i": game}).json()
        return result

    def get_game_extended(self, game: int) -> dict:
        """
        Get extended metadata about a game

        Params:
            i: The game ID to query
        """
        result = self._call_api("API_GetGameExtended.php?", {"i": game}).json()
        return result

    def get_achievement_count(self, game: int) -> dict:
        """
        Get the list of achievement ID's for a game

        Params:
            i: The game ID to query
        """
        result = self._call_api(
            "API_GetAchievementCount.php?", {"i": game}).json()
        return result

    def get_achievement_distribution(self, game: int) -> dict:
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

    def get_console_ids(self) -> list:
        """
        Get the complete list of console ID and name pairs on the site

        Params:
            None
        """
        result = self._call_api("API_GetConsoleIDs.php?", {}).json()
        return result

    def get_game_list(self, system: int, has_cheevos=0, hashes=0) -> dict:
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
