from typing import TypedDict


class AchievementOfTheWeekResponseEntity(TypedDict):
    ID: str
    Title: str
    Description: str
    Points: str
    TrueRatio: str
    Author: str
    DateCreated: str
    DateModified: str
    BadgeName: str
    BadgeURL: str


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
    RAPoints: str
    RASoftcorePoints: str
    DateAwarded: str
    HardcoreMode: str


class GetAchievementOfTheWeekResponse(TypedDict):
    Achievement: AchievementOfTheWeekResponseEntity
    Console: ConsoleEntity
    ForumTopic: ForumTopicEntity
    Game: GameEntity
    StartAt: str
    TotalPlayers: str
    Unlocks: list[UnlocksEntity]
    UnlocksCount: str
