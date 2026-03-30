from typing import TypedDict

from retroachievements.base import BaseRAClient


class GetUserRecentAchievementsEntity(TypedDict):
    Date: str
    HardcoreMode: int  # 0 or 1
    AchievementID: int
    Title: str
    Description: str
    BadgeName: str
    Points: int
    TrueRatio: int
    Type: str
    Author: str
    AuthorULID: str
    GameTitle: str
    GameIcon: str
    GameID: int
    ConsoleName: str
    BadgeURL: str
    GameURL: str


GetUserRecentAchievementsResponse = list[GetUserRecentAchievementsEntity]


def get_user_recent_achievements(
    self: BaseRAClient, username: str, recent_minutes: int | None = 60
) -> GetUserRecentAchievementsResponse:
    """
    A call to this method will retrieve a list of a target user's recently earned
    achievements, via their username. By default, it fetches achievements earned in the
    last hour.

    Params:
        username (str): The target username or ULID.
        recent_minutes (int): Minutes to look back. Defaults to 60.
    """
    result = self.call_api(
        "API_GetUserRecentAchievements.php?", {"u": username, "m": recent_minutes}
    ).json()
    return result
