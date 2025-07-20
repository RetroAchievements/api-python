from typing import TypedDict


class GetConsoleIdsResponseEntity(TypedDict):
    ID: str
    Name: str
    IconURL: str
    Active: bool
    IsGameSystem: bool


GetConsoleIdsResponse = list[GetConsoleIdsResponseEntity]
