import datetime
from typing import TypedDict

from retroachievements.base import BaseRAClient
from retroachievements.types import AchievementType


class DatedUserAchievementResponseEntity(TypedDict):
    Date: str
    HardcoreMode: str
    AchievementID: str
    Title: str
    Description: str
    BadgeName: str
    Points: str
    Type: AchievementType
    TrueRatio: int
    Author: str
    AuthorULID: str
    GameTitle: str
    GameIcon: str
    GameID: str
    ConsoleName: str
    CumulScore: int
    BadgeURL: str
    GameURL: str


DatedUserAchievementResponse = list[DatedUserAchievementResponseEntity]


def get_achievements_earned_between(
    self: BaseRAClient,
    username: str,
    from_datetime: datetime.datetime,
    to_datetime: datetime.datetime,
) -> DatedUserAchievementResponse:
    """
    A call to this method will retrieve a list of achievements earned by a given user
    between two provided dates.

    Params:
        username (str): The target username or ULID.
        from_datetime (datetime): A datetime object specifying when the list itself
                                  should begin.
        to_datetime (datetime):  A datetime object specifying when the list itself
                                 should end.
    """
    result = self.call_api(
        "API_GetAchievementsEarnedBetween.php?",
        {
            "u": username,
            "f": int(from_datetime.timestamp()),
            "t": int(to_datetime.timestamp()),
        },
    ).json()
    return result
