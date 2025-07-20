from typing import TypedDict


class LeaderboardEntryEntity(TypedDict):
    Rank: int
    User: str
    ULID: str
    Score: int
    FormattedScore: str
    DateSubmitted: str


class GetLeaderboardEntriesResponse(TypedDict):
    Count: int
    Total: int
    Results: list[LeaderboardEntryEntity]
