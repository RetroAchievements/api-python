from typing import TypedDict


class AchievementUnlocksResponseEntity(TypedDict):
    User: str
    ULID: str
    RAPoints: int
    RASoftcorePoints: int
    DateAwarded: str
    HardcoreMode: int


class GetAchievementUnlocksResponseEntity(TypedDict):
    ID: str
    Title: str
    Description: str
    Points: str
    TrueRatio: str
    Author: str
    DateCreated: str
    DateModified: str
    AuthorULID: str
    Type: str


class ConsoleEntity(TypedDict):
    ID: str
    Title: str


class GameEntity(TypedDict):
    ID: str
    Title: str


class GetAchievementUnlocksResponse(TypedDict):
    Achievement: GetAchievementUnlocksResponseEntity
    Console: ConsoleEntity
    Game: GameEntity
    UnlocksCount: int
    TotalPlayers: int
    UnlocksHardcoreCount: int
    Unlocks: list[AchievementUnlocksResponseEntity]
