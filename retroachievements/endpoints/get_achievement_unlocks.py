from typing import TypedDict


class AchievementUnlocksResponseEntity(TypedDict):
    User: str
    RAPoints: str
    RASoftcorePoints: str
    DateAwarded: str
    HardcoreMode: str


class GetAchievementUnlocksResponseEntity(TypedDict):
    ID: str
    Title: str
    Description: str
    Points: str
    TrueRatio: str
    Author: str
    DateCreated: str
    DateModified: str


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
    Unlocks: list[AchievementUnlocksResponseEntity]
