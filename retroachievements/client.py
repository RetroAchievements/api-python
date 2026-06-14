import datetime
import logging

from retroachievements.base import BaseRAClient
from retroachievements.endpoints.get_achievement_of_the_week import (
    GetAchievementOfTheWeekResponse,
)
from retroachievements.endpoints.get_achievement_ticket_stats import (
    GetAchievementTicketStatsResponse,
)
from retroachievements.endpoints.get_achievement_unlocks import (
    GetAchievementUnlocksResponse,
)
from retroachievements.endpoints.get_comments import GetCommentsResponse
from retroachievements.endpoints.get_console_ids import GetConsoleIdsResponse
from retroachievements.endpoints.get_developer_ticket_stats import (
    GetDeveloperTicketStatsResponse,
)
from retroachievements.endpoints.get_game_leaderboards_response import (
    GetGameLeaderboardsResponse,
)
from retroachievements.endpoints.get_game_list import GetGameListResponse
from retroachievements.endpoints.get_game_response import GetGameResponse
from retroachievements.endpoints.get_game_ticket_stats import GetGameTicketStatsResponse
from retroachievements.endpoints.get_leaderboard_entries_response import (
    GetLeaderboardEntriesResponse,
)
from retroachievements.endpoints.get_most_recent_tickets import (
    GetMostRecentTicketsResponse,
)
from retroachievements.endpoints.get_most_ticketed_games import (
    GetMostTicketedGamesResponse,
)
from retroachievements.endpoints.get_ticket_by_id import GetTicketByIdResponse
from retroachievements.endpoints.get_user_completed_games_response import (
    GetUserCompletedGamesResponse,
)
from retroachievements.endpoints.get_user_game_leaderboards_response import (
    GetUserGameLeaderboardsResponse,
)
from retroachievements.endpoints.get_user_set_requests_response import (
    GetUserSetRequestsResponse,
)
from retroachievements.endpoints.get_user_summary_response import GetUserSummaryResponse
from retroachievements.endpoints.get_user_want_to_play_list_response import (
    GetUserWantToPlayListResponse,
)
from retroachievements.endpoints.get_users_following_me_response import (
    GetUsersFollowingMeResponse,
)
from retroachievements.endpoints.get_users_i_follow_response import (
    GetUsersIFollowResponse,
)
from retroachievements.endpoints.user.get_achievements_earned_between import (
    DatedUserAchievementResponse,
    get_achievements_earned_between,
)
from retroachievements.endpoints.user.get_user_profile import (
    get_user_profile,
)
from retroachievements.endpoints.user.get_user_recent_achievements import (
    get_user_recent_achievements,
)
from retroachievements.types import (
    GameAwardKind,
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
    GetUserCompletionProgressResponse,
    GetUserGameRankAndScoreResponse,
    GetUserPointsResponse,
    GetUserProgressResponse,
    GetUserRecentlyPlayedGamesResponse,
)

logger = logging.getLogger(__name__)


class RAClient(BaseRAClient):
    # user endpoints

    def get_user_profile(self, username: str):
        return get_user_profile(self, username)

    def get_user_recent_achievements(
        self, username: str, recent_minutes: int | None = 60
    ):
        return get_user_recent_achievements(self, username, recent_minutes)

    def get_achievements_earned_between(
        self: BaseRAClient,
        username: str,
        from_datetime: datetime.datetime,
        to_datetime: datetime.datetime,
    ):
        return get_achievements_earned_between(
            self,
            username,
            from_datetime,
            to_datetime,
        )

    def get_user_achievements_earned_on_day(
        self, user: str, date: str
    ) -> DatedUserAchievementResponse:
        """
        Get a user's achievements earned on a specific day

        Params:
            u: Username or ULID to query
            d: Date in YYYY-MM-DD format, default = now
        """
        result = self.call_api(
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
        result = self.call_api(
            "API_GetGameInfoAndUserProgress.php?", {"u": user, "g": game, "a": awards}
        ).json()
        return result

    def get_user_completion_progress(
        self, user: str, count: int = 100, offset: int = 0
    ) -> GetUserCompletionProgressResponse:
        """
        Get a user's completion progress in games

        Params:
            u: Username or ULID to query
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self.call_api(
            "API_GetUserCompletionProgress.php?", {"u": user, "c": count, "o": offset}
        ).json()
        return result

    def get_user_awards(self, user: str) -> GetUserAwardsResponse:
        """
        Get a user's awards

        Params:
            u: Username or ULID to query
        """
        result = self.call_api("API_GetUserAwards.php?", {"u": user}).json()
        return result

    def get_user_claims(self, user: str) -> GetUserClaimsResponse:
        """
        Get a user's claims

        Params:
            u: Username or ULID to query
        """
        result = self.call_api("API_GetUserClaims.php?", {"u": user}).json()
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
        result = self.call_api(
            "API_GetUserGameRankAndScore.php?", {"u": user, "g": game}
        ).json()
        return result

    def get_user_points(self, user: str) -> GetUserPointsResponse:
        """
        Get a user's total hardcore and softcore points

        Params:
            u: Username or ULID to query
        """
        result = self.call_api("API_GetUserPoints.php?", {"u": user}).json()
        return result

    def get_user_progress(self, user: str, games: list[int]) -> GetUserProgressResponse:
        """
        Get a user's progress in a game.

        Params:
            u: Username or ULID to query.
            i: List of games IDs to query separated by a comma.
        """
        logger.warning(
            "Unless you are explicitly wanting summary progress details for specific "
            "game IDs, get_user_completion_progress will almost certainly be "
            "better-suited for your use case."
        )
        result = self.call_api(
            "API_GetUserProgress.php?",
            {"u": user, "i": ",".join([str(game) for game in games])},
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
        result = self.call_api(
            "API_GetUserRecentlyPlayedGames.php?", {"u": user, "c": count, "o": offset}
        ).json()
        return result

    def get_user_summary(
        self, user: str, games_count: int = 0, achievements_count: int = 10
    ) -> GetUserSummaryResponse:
        """
        Get a user's exhaustive profile metadata

        Params:
            u: Username or ULID to query
            g: Number of recent games to fetch, default = 0
            a: Number of recent achievements to fetch, default = 10
        """
        logger.warning(
            "This endpoint is known to be slow, and often results in over-fetching. For "
            "basic user profile information, try the get_user_profile endpoint. For user "
            "completion and game progress information, try the "
            "get_user_completion_progress endpoint. Recent achievements are pulled from "
            "recent games, so if you ask for 1 game and 10 achievements, and the user "
            "has only earned 8 achievements in the most recent game, you'll only get 8 "
            "recent achievements back. Similarly, with the default of 0 recent games, no "
            "recent achievements will be returned.",
        )
        result = self.call_api(
            "API_GetUserSummary.php?",
            {"u": user, "g": games_count, "a": achievements_count},
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
        logger.warning(
            "This endpoint is considered 'legacy'. The get_user_completion_progress "
            "endpoint will almost always be a better fit for your use case."
        )
        result = self.call_api("API_GetUserCompletedGames.php?", {"u": user}).json()
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
        result = self.call_api(
            "API_GetUserWantToPlayList.php?", {"u": user, "c": count, "o": offset}
        ).json()
        return result

    def get_users_i_follow(
        self, count: int = 100, offset: int = 0
    ) -> GetUsersIFollowResponse:
        """
        Get a list of users that the specified user follows

        Params:
            u: Username or ULID to query
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self.call_api(
            "API_GetUsersIFollow.php?", {"c": count, "o": offset}
        ).json()
        return result

    def get_users_following_me(
        self, count: int = 100, offset: int = 0
    ) -> GetUsersFollowingMeResponse:
        """
        Get a list of users that follow the specified user

        Params:
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self.call_api(
            "API_GetUsersFollowingMe.php?", {"c": count, "o": offset}
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

        result = self.call_api(
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
        result = self.call_api("API_GetGame.php?", {"i": game}).json()
        return result

    def get_game_extended(
        self, game: int, get_unofficial_achievements: bool = False
    ) -> GetGameExtendedResponse:
        """
        Get extended metadata about a game

        Params:
            i: The game ID to query
            f: Set to 3 for Official achievements, 5 to see Unofficial / Demoted achievements, default = 3
        """
        unofficial = 5 if get_unofficial_achievements else 3
        result = self.call_api(
            "API_GetGameExtended.php?", {"i": game, "f": unofficial}
        ).json()
        return result

    def get_game_hashes(self, game: int) -> GetGameHashesResponse:
        """
        Get the hashes for a game

        Params:
            i: The game ID to query
        """
        result = self.call_api("API_GetGameHashes.php?", {"i": game}).json()
        return result

    def get_achievement_count(self, game: int) -> GetAchievementCountResponse:
        """
        Get the list of achievement ID's for a game

        Params:
            i: The game ID to query
        """
        result = self.call_api("API_GetAchievementCount.php?", {"i": game}).json()
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
        result = self.call_api(
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
            t: 1 for latest masters. 0 for non-master high scores. Defaults to 0.
        """
        if list_type not in [0, 1]:
            raise ValueError("Invalid list type. Must be 0 or 1.")
        result = self.call_api(
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
        result = self.call_api(
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
        result = self.call_api(
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
        result = self.call_api(
            "API_GetUserGameLeaderboards.php?",
            {"i": game, "u": user, "c": count, "o": offset},
        ).json()
        return result

    # System Endpoints

    def get_console_ids(
        self, active_systems_only: bool = False, gaming_systems_only: bool = False
    ) -> GetConsoleIdsResponse:
        """
        Get the complete list of console ID and name pairs on the site

        Params:
            a: If 1, only return active systems. Defaults to 0.
            g: If 1, only return gaming systems (not Hubs, Events, etc). Defaults to 0.
        """
        result = self.call_api(
            "API_GetConsoleIDs.php?",
            {"a": int(active_systems_only), "g": int(gaming_systems_only)},
        ).json()
        return result

    def get_game_list(
        self,
        system: int,
        has_achievements: int = 0,
        hashes: int = 0,
        offset: int = 0,
        count: int = 0,
    ) -> GetGameListResponse:
        """
        Get the complete list of games for a console

        Params:
            i: The system ID to query
            f: If 1, only returns games that have achievements (default = 0)
            h: If 1, also return the supported hashes for games (default = 0)
            o: Offset of the list of results. Ignores the first X results set in this parameter. Defaults to 0. Useful for pagination.
            c: Number of max results desired. Defaults to 0, which means, all the results. Useful for pagination.
        """
        if has_achievements not in [0, 1]:
            raise ValueError("Invalid has_cheevos value. Must be 0 or 1.")
        if hashes not in [0, 1]:
            raise ValueError("Invalid hashes value. Must be 0 or 1.")
        result = self.call_api(
            "API_GetGameList.php?",
            {"i": system, "f": has_achievements, "h": hashes, "o": offset, "c": count},
        ).json()
        return result

    # Achievement Endpoints

    def get_achievement_unlocks(
        self, achievement: int, count: int = 50, offset: int = 0
    ) -> GetAchievementUnlocksResponse:
        """
        Get the unlocks for an achievement

        Params:
            a: The achievement ID to query
            c: Count, the number of records to return (default = 50, max = 500)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self.call_api(
            "API_GetAchievementUnlocks.php?",
            {"a": achievement, "c": count, "o": offset},
        ).json()
        return result

    # Comment Endpoints

    def get_comments(
        self,
        target_id: int | str,
        target_kind: int,
        count: int = 100,
        offset: int = 0,
        sort: str = "submitted",
    ) -> GetCommentsResponse:
        """
        Get comments for a game or achievement

        Params:
            i: The target game or achievement ID (if type is 1 or 2). The target username or user ULID (if type is 3).
            t: The target comment kind: 1 (game), 2 (achievement), or 3 (user). Required if type is 1 or 2.
            c: Count, the number of records to return (default = 100, max = 500)
            o: Offset, the number of entries to skip (default = 0)
            sort: Sort order, submitted = ascending, -submitted = descending, default = 'submitted'
        """
        if target_kind not in [1, 2, 3]:
            raise ValueError(
                "Invalid target type. Must be 1 (game), 2 (achievement), or 3 (user/ulid)."
            )
        if sort not in ["submitted", "-submitted"]:
            raise ValueError("Invalid sort order. Must be 'submitted' or '-submitted'.")
        result = self.call_api(
            "API_GetComments.php?",
            {"i": target_id, "t": target_kind, "c": count, "o": offset, "sort": sort},
        ).json()
        return result

    # Feed Endpoints
    def get_recent_game_awards(
        self,
        date: str | None = None,
        offset: int = 0,
        count: int = 25,
        kinds: list[GameAwardKind] | None = None,
    ) -> GetRecentGameAwardsResponse:
        """
        Get recent game awards

        Params:
            d: Date in YYYY-MM-DD format, default = now
            o: Offset, the number of entries to skip (default = 0)
            c: Count, the number of records to return (default = 25, max = 100)
            k: A comma-separated list of desired game award kinds. Possible values are "beaten-softcore", "beaten-hardcore", "completed", and "mastered" (default: all game award kinds).
        """
        if date is None:
            date = datetime.date.today().strftime("%Y-%m-%d")
        if kinds is None:
            kinds = [
                "beaten-softcore",
                "beaten-hardcore",
                "completed",
                "mastered",
            ]

        result = self.call_api(
            "API_GetRecentGameAwards.php?",
            {"d": date, "o": offset, "c": count, "k": ",".join(kinds)},
        ).json()
        return result

    def get_active_claims(self) -> GetSetClaimsResponse:
        """
        Get the list of active active claims (1000 max)

        Params:
            None
        """
        result = self.call_api("API_GetActiveClaims.php?", {}).json()
        return result

    def get_top_ten_users(self) -> GetTopTenUsersResponse:
        """
        Get the top ten users on the site

        Params:
            None
        """
        result = self.call_api("API_GetTopTenUsers.php?", {}).json()
        return result

    # Event Endpoints

    def get_achievement_of_the_week(self) -> GetAchievementOfTheWeekResponse:
        """
        Get the achievement of the week

        Params:
            None
        """
        result = self.call_api("API_GetAchievementOfTheWeek.php?", {}).json()
        return result

    # Ticket Endpoints

    def get_ticket_by_id(self, ticket_id: int) -> GetTicketByIdResponse:
        """
        Get the data for a specific ticket

        Params:
            i: The ticket ID to query
        """
        result = self.call_api("API_GetTicketData.php?", {"i": ticket_id}).json()
        return result

    def get_most_ticketed_games(
        self, focus: int = 1, count: int = 10, offset: int = 0
    ) -> GetMostTicketedGamesResponse:
        """
        Get the most ticketed games

        Params:
            f: Must be set to 1.
            c: Count, number of records to return (default: 10, max: 100).
            o: Offset, number of entries to skip (default: 0).
        """
        result = self.call_api(
            "API_GetTicketData.php?", {"f": focus, "c": count, "o": offset}
        ).json()
        return result

    def get_most_recent_tickets(
        self, count: int = 10, offset: int = 0
    ) -> GetMostRecentTicketsResponse:
        """
        Get the most recent tickets

        Params:
            c: Count, the number of records to return (default = 10, max = 100)
            o: Offset, the number of entries to skip (default = 0)
        """
        result = self.call_api(
            "API_GetTicketData.php?", {"c": count, "o": offset}
        ).json()
        return result

    def get_game_ticket_stats(
        self, game: int, focus: int = 3, depth: int = 0
    ) -> GetGameTicketStatsResponse:
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
        result = self.call_api(
            "API_GetTicketData.php?", {"g": game, "f": focus, "d": depth}
        ).json()
        return result

    def get_developer_ticket_stats(
        self, username: str
    ) -> GetDeveloperTicketStatsResponse:
        """
        Get the ticket stats for a developer

        Params:
            u: The target developer's username or ULID.
        """
        result = self.call_api("API_GetTicketData.php?", {"u": username}).json()
        return result

    def get_achievement_ticket_stats(
        self, achievement: int
    ) -> GetAchievementTicketStatsResponse:
        """
        Get the ticket stats for an achievement

        Params:
            a: The achievement ID to query
        """
        result = self.call_api("API_GetTicketData.php?", {"a": achievement}).json()
        return result
