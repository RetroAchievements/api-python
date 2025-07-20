from typing import TypedDict


class UserWantToPlayListEntity(TypedDict):
    ID: int
    Title: str
    ImageIcon: str
    ConsoleID: int
    ConsoleName: str
    PointsTotal: int
    AchievementsPublished: int


class GetUserWantToPlayListResponse(TypedDict):
    Count: int
    Total: int
    Results: list[UserWantToPlayListEntity]
