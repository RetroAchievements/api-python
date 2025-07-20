import datetime
import warnings

import requests

from retroachievements import __version__
from retroachievements.models.get_game_leaderboards_response import (
    GetGameLeaderboardsResponse,
)
from retroachievements.models.get_game_response import GetGameResponse
from retroachievements.models.get_leaderboard_entries_response import (
    GetLeaderboardEntriesResponse,
)
from retroachievements.models.get_user_completed_games_response import (
    GetUserCompletedGamesResponse,
)
from retroachievements.models.get_user_game_leaderboards_response import (
    GetUserGameLeaderboardsResponse,
)
from retroachievements.models.get_user_set_requests_response import (
    GetUserSetRequestsResponse,
)
from retroachievements.models.get_user_summary_response import GetUserSummaryResponse
from retroachievements.models.get_user_want_to_play_list_response import (
    GetUserWantToPlayListResponse,
)
from retroachievements.models.get_users_following_me_response import (
    GetUsersFollowingMeResponse,
)
from retroachievements.models.get_users_i_follow_response import GetUsersIFollowResponse
from retroachievements.types import (
    DatedUserAchievementResponse,
    GetAchievementCountResponse,
    GetAchievementDistributionResponse,
    GetGameExtendedResponse,
    GetGameHashesResponse,
    GetGameInfoAndUserProgressResponse,
    GetGameRankAndScoreResponse,
    GetRecentGameAwardsResponse,
    GetSetClaimsResponse,
    GetTopTenUsersResponse,
    GetUserAwardsResponse,
    GetUserClaimsResponse,
    GetUserCompletionProgressResponseEntity,
    GetUserGameRankAndScoreResponse,
    GetUserPointsResponse,
    GetUserProgressResponse,
    GetUserRecentAchievementsResponse,
    GetUserRecentlyPlayedGamesResponse,
    UserProfileResponse,
)

_BASE_URL = "https://retroachievements.org/API/"


class RAClient:
    """
    Main class for accessing the RetroAchievements Web API
    """

    headers = {"User-Agent": "RetroAchievements-api-python/" + __version__}

    def __init__(self, api_key: str):
        self.api_key = api_key

    def url_params(self, params: dict[str, str | int | None] | None = None):
        """
        Inserts the auth and query params into the request
        """
        if params is None:
            params = {}
        params.update({"y": self.api_key})
        return params

    def is_valid_game_csv(self, value: str | int) -> bool:
        """
        Validates if the given value is a valid game CSV string or integer.

        Example of valid game CSV:
          12345,
          "12345"
          "12345, 67890"
          "123, 456, 789"

        Example of invalid game ID:
          "123a"
          "123,,456"
          "123, "
        """
        if isinstance(value, int):
            return True
        parts = value.split(",")
        return all(part.strip().isdigit() for part in parts if part)

    # URL construction
    def _call_api(
        self,
        endpoint: str | None = None,
        params: dict[str, str | int | None] | None = None,
        timeout: int = 30,
        headers: dict[str, str] | None = None,
    ):
        if endpoint is None:
            endpoint = ""
        req = requests.get(
            f"{_BASE_URL}{endpoint}",
            params=self.url_params(params),
            timeout=timeout,
            headers=headers,
        )
        return req

    # User endpoints

    def get_user_profile(self, user: str, ulid: str) -> UserProfileResponse:
        """
        Get a user's profile information

        Params:
            u: Username to query
            i: ULID to query
        """
        result = self._call_api(
            "API_GetUserProfile.php?", {"u": user, "i": ulid}
        ).json()
        return result

    def get_user_recent_achievements(
        self, user: str, minutes: int = 60
    ) -> GetUserRecentAchievementsResponse:
        """
        Get a user's recent achievements

        Params:
            u: Username or ULID to query
            m: Minutes to look back, default = 60
        """
        result = self._call_api(
            "API_GetUserRecentAchievements.php?", {"u": user, "m": minutes}
        ).json()
        return result

    def get_user_achievements_earned_between(
        self, user: str, start: int, end: int
    ) -> DatedUserAchievementResponse:
        """
        Get a user's achievements in a range

        Params:
            u: Username or ULID to query
            f: Epoch timestamp. Time range start.
            t: Epoch timestamp. Time range end.
        """
        result = self._call_api(
            "API_GetAchievementsEarnedBetween.php?", {"u": user, "s": start, "e": end}
        ).json()
        return result

    def get_user_achievements_earned_on_day(
        self, user: str, date: str
    ) -> DatedUserAchievementResponse:
        """
        Get a user's achievements earned on a specific day

        Params:
            u: Username or ULID to query
            d: Date in YYYY-MM-DD format, default = now
        """
        result = self._call_api(
            "API_GetAchievementsEarnedOnDay.php?", {"u": user, "d": date}
        ).json()
        return result

    def get_game_info_and_user_progress(
        self, user: str, game: int, awards: int = 0
    ) -> GetGameInfoAndUserProgressResponse:
        """
        Get a user's progress in a game, including game metadata

        Params:
            u: Username or ULID to query
            g: Game ID to query
            a: If set to 1 also return the user's awards, default = 0
        """
        if awards not in [0, 1]:
            raise ValueError("Invalid awards value. Must be 0 or 1.")
        result = self._call_api(
            "API_GetGameInfoAndUserProgress.php?", {"u": user, "g": game, "a": awards}
        ).json()
        return result

    def get_user_completion_progress(
        self, user: str, count: int = 100, offset: int = 0
    ) -> GetUserCompletionProgressResponseEntity:
        """
        Get a user's completion progress in games

        Params:
            u: Username or ULID to query
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self._call_api(
            "API_GetUserCompletionProgress.php?", {"u": user, "c": count, "o": offset}
        ).json()
        return result

    def get_user_awards(self, user: str) -> GetUserAwardsResponse:
        """
        Get a user's awards

        Params:
            u: Username or ULID to query
        """
        result = self._call_api("API_GetUserAwards.php?", {"u": user}).json()
        return result

    def get_user_claims(self, user: str) -> GetUserClaimsResponse:
        """
        Get a user's claims

        Params:
            u: Username or ULID to query
        """
        result = self._call_api("API_GetUserClaims.php?", {"u": user}).json()
        return result

    def get_user_game_rank_and_score(
        self, user: str, game: int
    ) -> GetUserGameRankAndScoreResponse:
        """
        Get a user's rank and score in a game

        Params:
            u: Username or ULID to query
            g: Game ID to query
        """
        result = self._call_api(
            "API_GetUserGameRankAndScore.php?", {"u": user, "g": game}
        ).json()
        return result

    def get_user_points(self, user: str) -> GetUserPointsResponse:
        """
        Get a user's total hardcore and softcore points

        Params:
            u: Username or ULID to query
        """
        result = self._call_api("API_GetUserPoints.php?", {"u": user}).json()
        return result

    def get_user_progress(self, user: str, game: str | int) -> GetUserProgressResponse:
        """
        Get a user's progress in a game

        Params:
            u: Username or ULID to query
            i: Game ID to query

        Information:
            Unless you are explicitly wanting summary progress details for specific game IDs, get_user_completion_progress will almost certainly be better-suited for your use case.
        """
        warnings.warn(
            "Unless you are explicitly wanting summary progress details for specific game IDs, get_user_completion_progress will almost certainly be better-suited for your use case.",
            Warning,
            stacklevel=2,
        )
        if not self.is_valid_game_csv(game):
            raise ValueError("Invalid game ID or CSV format")

        result = self._call_api(
            "API_GetUserProgress.php?", {"u": user, "i": game}
        ).json()
        return result

    def get_user_recently_played_games(
        self, user: str, count: int = 10, offset: int = 0
    ) -> GetUserRecentlyPlayedGamesResponse:
        """
        Get a user's recently played games

        Params:
            u: Username or ULID to query
            c: Count, the number of records to return (default = 10, max = 50)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self._call_api(
            "API_GetUserRecentlyPlayedGames.php?", {"u": user, "c": count, "o": offset}
        ).json()
        return result

    def get_user_summary(
        self, user: str, games: int = 0, achievements: int = 10
    ) -> GetUserSummaryResponse:
        """
        Get a user's exhaustive profile metadata

        Params:
            u: Username or ULID to query
            g: Number of recent games to fetch, default = 0
            a: Number of recent achievements to fetch, default = 10

        Information:
            This endpoint is known to be slow, and often results in over-fetching. For basic user profile information, try the get_user_profile endpoint. For user completion and game progress information, try the get_user_completion_progress endpoint.

            Recent achievements are pulled from recent games, so if you ask for 1 game and 10 achievements, and the user has only earned 8 achievements in the most recent game, you'll only get 8 recent achievements back. Similarly, with the default of 0 recent games, no recent achievements will be returned.
        """
        warnings.warn(
            "This endpoint is known to be slow, and often results in over-fetching. For basic user profile information, try the get_user_profile endpoint. For user completion and game progress information, try the get_user_completion_progress endpoint."
            "Recent achievements are pulled from recent games, so if you ask for 1 game and 10 achievements, and the user has only earned 8 achievements in the most recent game, you'll only get 8 recent achievements back. Similarly, with the default of 0 recent games, no recent achievements will be returned.",
            Warning,
            stacklevel=2,
        )
        result = self._call_api(
            "API_GetUserSummary.php?",
            {"u": user, "g": games, "a": achievements},
        ).json()
        return result

    def get_user_completed_games(self, user: str) -> GetUserCompletedGamesResponse:
        """
        Get a user's completed games

        Params:
            u: Username or ULID to query

        Information:
            This endpoint is considered "legacy". The get_user_completion_progress endpoint will almost always be a better fit for your use case.
        """
        warnings.warn(
            "This endpoint is considered 'legacy'. The get_user_completion_progress endpoint will almost always be a better fit for your use case.",
            DeprecationWarning,
            stacklevel=2,
        )
        result = self._call_api("API_GetUserCompletedGames.php?", {"u": user}).json()
        return result

    def get_user_want_to_play_list(
        self, user: str, count: int = 100, offset: int = 0
    ) -> GetUserWantToPlayListResponse:
        """
        Get a user's 'Want to Play' list

        Params:
            u: Username or ULID to query
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self._call_api(
            "API_GetUserWantToPlayList.php?", {"u": user, "c": count, "o": offset}
        ).json()
        return result

    def get_users_i_follow(
        self, user: str, count: int = 100, offset: int = 0
    ) -> GetUsersIFollowResponse:
        """
        Get a list of users that the specified user follows

        Params:
            u: Username or ULID to query
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self._call_api(
            "API_GetUsersIFollow.php?", {"u": user, "c": count, "o": offset}
        ).json()
        return result

    def get_users_following_me(
        self, user: str, count: int = 100, offset: int = 0
    ) -> GetUsersFollowingMeResponse:
        """
        Get a list of users that follow the specified user

        Params:
            u: Username or ULID to query
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self._call_api(
            "API_GetUsersFollowingMe.php?", {"u": user, "c": count, "o": offset}
        ).json()
        return result

    def get_user_set_requests(
        self, user: str, list_type: int = 0
    ) -> GetUserSetRequestsResponse:
        """
        Get a user's set requests

        Params:
            u: Username or ULID to query
            t: List type: 0 for active requests, 1 for all requests, default = 0
        """
        if list_type not in [0, 1]:
            raise ValueError("Invalid list type. Must be 0 or 1.")

        result = self._call_api(
            "API_GetUserSetRequests.php?", {"u": user, "t": list_type}
        ).json()
        return result

    # Game endpoints

    def get_game(self, game: int) -> GetGameResponse:
        """
        Get basic metadata about a game

        Params:
            i: The game ID to query
        """
        result = self._call_api("API_GetGame.php?", {"i": game}).json()
        return result

    def get_game_extended(self, game: int, focus: int = 3) -> GetGameExtendedResponse:
        """
        Get extended metadata about a game

        Params:
            i: The game ID to query
            f: Set to 3 for Official achievements, 5 to see Unofficial / Demoted achievements, default = 3
        """
        if focus not in [3, 5]:
            raise ValueError("Invalid set type selected. Must be 3 or 5.")
        result = self._call_api(
            "API_GetGameExtended.php?", {"i": game, "f": focus}
        ).json()
        return result

    def get_game_hashes(self, game: int) -> GetGameHashesResponse:
        """
        Get the hashes for a game

        Params:
            i: The game ID to query
        """
        result = self._call_api("API_GetGameHashes.php?", {"i": game}).json()
        return result

    def get_achievement_count(self, game: int) -> GetAchievementCountResponse:
        """
        Get the list of achievement ID's for a game

        Params:
            i: The game ID to query
        """
        result = self._call_api("API_GetAchievementCount.php?", {"i": game}).json()
        return result

    def get_achievement_distribution(
        self, game: int, achievement_type: int = 0, focus: int = 3
    ) -> GetAchievementDistributionResponse:
        """
        Get how many players have unlocked how many achievements for a game

        Params:
            i: The game ID to query
            h: Set to 1 to only query hardcore unlocks, 0 to query all unlocks, default = 0
            f: Set to 3 for Official achievements, 5 for Unofficial / Demoted achievements, default = 3
        """
        if achievement_type not in [0, 1]:
            raise ValueError("Invalid achievement type. Must be 0 or 1.")
        if focus not in [3, 5]:
            raise ValueError("Invalid set type selected. Must be 3 or 5.")
        result = self._call_api(
            "API_GetAchievementDistribution.php?",
            {"i": game, "h": achievement_type, "f": focus},
        ).json()
        return result

    def get_game_rank_and_score(
        self, game: int, list_type: int = 0
    ) -> GetGameRankAndScoreResponse:
        """
        Get the rank and score for a game

        Params:
            g: The game ID to query
            t: Set to 0 for Latest Masters, 1 for High Scores, default = 0
        """
        if list_type not in [0, 1]:
            raise ValueError("Invalid list type. Must be 0 or 1.")
        result = self._call_api(
            "API_GetGameRankAndScore.php?", {"g": game, "t": list_type}
        ).json()
        return result

    # Leaderboard Endpoints

    def get_game_leaderboards(
        self, game: int, count: int = 100, offset: int = 0
    ) -> GetGameLeaderboardsResponse:
        """
        Get the leaderboards for a game

        Params:
            i: The game ID to query
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self._call_api(
            "API_GetGameLeaderboards.php?", {"i": game, "c": count, "o": offset}
        ).json()
        return result

    def get_leaderboard_entries(
        self, leaderboard: int, count: int = 100, offset: int = 0
    ) -> GetLeaderboardEntriesResponse:
        """
        Get the entries of a leaderboard

        Params:
            i: The leaderboard ID to query
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self._call_api(
            "API_GetLeaderboardEntries.php?",
            {"i": leaderboard, "c": count, "o": offset},
        ).json()
        return result

    def get_user_game_leaderboards(
        self, game: int, user: str, count: int = 200, offset: int = 0
    ) -> GetUserGameLeaderboardsResponse:
        """
        Get a user's leaderboard entries for a game

        Params:
            i: Game ID to query
            u: Username or ULID to query
            c: Count, the number of records to return (default = 200, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self._call_api(
            "API_GetUserGameLeaderboards.php?",
            {"i": game, "u": user, "c": count, "o": offset},
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

    def get_game_list(
        self, system: int, has_achievements: int = 0, hashes: int = 0
    ) -> dict:
        """
        Get the complete list of games for a console

        Params:
            i: The system ID to query
            f: If 1, only returns games that have achievements (default = 0)
            h: If 1, also return the supported hashes for games (default = 0)
        """
        if has_achievements not in [0, 1]:
            raise ValueError("Invalid has_cheevos value. Must be 0 or 1.")
        if hashes not in [0, 1]:
            raise ValueError("Invalid hashes value. Must be 0 or 1.")
        result = self._call_api(
            "API_GetGameList.php?", {"i": system, "f": has_achievements, "h": hashes}
        ).json()
        return result

    # Achievement Endpoints

    def get_achievement_unlocks(
        self, achievement: int, count: int = 50, offset: int = 0
    ) -> dict:
        """
        Get the unlocks for an achievement

        Params:
            a: The achievement ID to query
            c: Count, the number of records to return (default = 50, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self._call_api(
            "API_GetAchievementUnlocks.php?",
            {"a": achievement, "c": count, "o": offset},
        ).json()
        return result

    # Comment Endpoints

    def get_comments(
        self,
        game: int,
        target: int,
        count: int = 100,
        offset: int = 0,
        sort: str = "submitted",
    ) -> dict:
        """
        Get comments for a game or achievement

        Params:
            i: The game ID to query
            t: The target ID (game = 1, achievement = 2, user/ulid = 3)
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
            sort: Sort order, submitted = ascending, -submitted = descending, default = 'submitted'
        """
        if target not in [1, 2, 3]:
            raise ValueError(
                "Invalid target type. Must be 1 (game), 2 (achievement), or 3 (user/ulid)."
            )
        if sort not in ["submitted", "-submitted"]:
            raise ValueError("Invalid sort order. Must be 'submitted' or '-submitted'.")
        result = self._call_api(
            "API_GetComments.php?",
            {"i": game, "t": target, "c": count, "o": offset, "sort": sort},
        ).json()
        return result

    # Feed Endpoints
    def get_recent_game_awards(
        self,
        date: str | None = None,
        offset: int = 0,
        count: int = 25,
        kind: str | None = None,
    ) -> GetRecentGameAwardsResponse:
        """
        Get recent game awards

        Params:
            d: Date in YYYY-MM-DD format, default = now
            o: Offset, the number of entries to skip (default = 0)
            c: Count, the number of records to return (default = 25, max = 100)
            k: Type of award to filter by (optional), possible values are 'beaten-softcore', 'beaten-hardcore', 'completed' and 'mastered'. If not specified, all awards will be returned.
        """
        if date is None:
            date = datetime.date.today().strftime("%Y-%m-%d")
        if kind is not None and kind not in [
            "beaten-softcore",
            "beaten-hardcore",
            "completed",
            "mastered",
        ]:
            raise ValueError(
                "Invalid kind value. Must be one of 'beaten-softcore', 'beaten-hardcore', 'completed', or 'mastered'."
            )
        result = self._call_api(
            "API_GetRecentGameAwards.php?",
            {"d": date, "o": offset, "c": count, "k": kind},
        ).json()
        return result

    def get_active_claims(self) -> GetSetClaimsResponse:
        """
        Get the list of active active claims (1000 max)

        Params:
            None
        """
        result = self._call_api("API_GetActiveClaims.php?", {}).json()
        return result

    def get_inactive_claims(self, kind: int = 1) -> GetSetClaimsResponse:
        """
        Get the list of inactive claims, inactive claims are claims that have been completed, dropped or expired.

        Params:
            k: Kind of claim to return, 1 (completed), 2 (dropped), 3 (expired), default = 1
        """
        if kind not in [1, 2, 3]:
            raise ValueError(
                "Invalid kind value. Must be 1 (completed), 2 (dropped) or 3 (expired)."
            )
        result = self._call_api("API_GetInactiveClaims.php?", {"k": kind}).json()
        return result

    def get_top_ten_users(self) -> GetTopTenUsersResponse:
        """
        Get the top ten users on the site

        Params:
            None
        """
        result = self._call_api("API_GetTopTenUsers.php?", {}).json()
        return result

    # Event Endpoints

    def get_achievement_of_the_week(self) -> dict:
        """
        Get the achievement of the week

        Params:
            None
        """
        result = self._call_api("API_GetAchievementOfTheWeek.php?", {}).json()
        return result

    # Ticket Endpoints

    def get_ticket_data(self, ticket_id: int) -> dict:
        """
        Get the data for a specific ticket

        Params:
            i: The ticket ID to query
        """
        result = self._call_api("API_GetTicketData.php?", {"i": ticket_id}).json()
        return result

    def get_most_ticketed_games(self, focus: int = 1) -> dict:
        """
        Get the most ticketed games

        Params:
            f: Must be set to 1.
        """
        result = self._call_api("API_GetTicketData.php?", {"f": focus}).json()
        return result

    def get_most_recent_tickets(self, count: int = 10, offset: int = 0) -> dict:
        """
        Get the most recent tickets

        Params:
            c: Count, the number of records to return (default = 10, max = 100)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self._call_api(
            "API_GetTicketData.php?", {"c": count, "o": offset}
        ).json()
        return result

    def get_game_ticket_stats(self, game: int, focus: int = 3, depth: int = 0) -> dict:
        """
        Get the ticket stats for a game

        Params:
            g: The game ID to query
            f: Focus, 3 for official tickets, 5 for unofficial tickets, default = 3
            d: Depth, 0 for basic stats, 1 for deep ticket metadata in the responses Tickets array, default = 0
        """
        if focus not in [3, 5]:
            raise ValueError(
                "Invalid focus value. Must be 3 (official) or 5 (unofficial)."
            )
        result = self._call_api(
            "API_GetTicketData.php?", {"g": game, "f": focus, "d": depth}
        ).json()
        return result

    def get_developer_ticket_stats(self, username: str, ulid: str) -> dict:
        """
        Get the ticket stats for a developer

        Params:
            u: Username or ULID to query
            i: ULID to query
        """
        result = self._call_api(
            "API_GetTicketData.php?", {"u": username, "i": ulid}
        ).json()
        return result

    def get_achievement_ticket_stats(self, achievement: int) -> dict:
        """
        Get the ticket stats for an achievement

        Params:
            a: The achievement ID to query
        """
        result = self._call_api("API_GetTicketData.php?", {"a": achievement}).json()
        return result
