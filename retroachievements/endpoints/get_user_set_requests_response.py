from typing import TypedDict


class UserSetRequestEntity(TypedDict):
    GameID: int
    Title: str
    ConsoleID: int
    ConsoleName: str
    ImageIcon: str


class GetUserSetRequestsResponse(TypedDict):
    RequestedSets: list[UserSetRequestEntity]
    TotalRequests: int
    PointsForNext: int
