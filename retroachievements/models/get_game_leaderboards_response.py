from typing import TypedDict


class TopEntryEntity(TypedDict):
    User: str
    ULID: str
    Score: str
    FormattedScore: str


class GetGameLeaderboardsResponseEntity(TypedDict):
    ID: int
    RankAsc: bool
    Title: str
    Description: str
    Format: str
    Author: str
    AuthorULID: str
    TopEntry: TopEntryEntity


class GetGameLeaderboardsResponse(TypedDict):
    Count: int
    Total: int
    Results: list[GetGameLeaderboardsResponseEntity]
