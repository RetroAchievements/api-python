from typing import TypedDict


class UserEntryEntity(TypedDict):
    User: str
    ULID: str
    Score: int
    FormattedScore: str
    Rank: int
    DateUpdated: str


class GetUserGameLeaderboardsResponseEntity(TypedDict):
    ID: int
    RankAsc: bool
    Title: str
    Description: str
    Format: str
    UserEntry: UserEntryEntity


class GetUserGameLeaderboardsResponse(TypedDict):
    Count: int
    Total: int
    Results: list[GetUserGameLeaderboardsResponseEntity]
