from typing import TypedDict


class RawGameListEntity(TypedDict):
    Title: str
    ID: int
    ConsoleID: int
    ConsoleName: str
    ImageIcon: str
    NumAchievements: int
    NumLeaderboards: int
    Points: int
    DateModified: str
    ForumTopicID: int
    Hashes: list[str] | None


GetGameListResponse = list[RawGameListEntity]
