from typing import TypedDict


class AchievementOfTheWeekResponseEntity(TypedDict):
    ID: str
    Title: str
    Description: str
    Points: int
    TrueRatio: int
    Type: str | None
    Author: str
    AuthorULID: str
    DateCreated: str
    DateModified: str


class ConsoleEntity(TypedDict):
    ID: str
    Title: str


class ForumTopicEntity(TypedDict):
    ID: int


class GameEntity(TypedDict):
    ID: str
    Title: str


class UnlocksEntity(TypedDict):
    User: str
    ULID: str
    RAPoints: int
    RASoftcorePoints: int
    DateAwarded: str
    HardcoreMode: int


class GetAchievementOfTheWeekResponse(TypedDict):
    Achievement: AchievementOfTheWeekResponseEntity
    Console: ConsoleEntity
    ForumTopic: ForumTopicEntity
    Game: GameEntity
    StartAt: str
    TotalPlayers: int
    Unlocks: list[UnlocksEntity]
    UnlocksCount: int
    UnlocksHardcoreCount: int
