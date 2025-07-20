from typing import Literal, TypedDict


class UserCompletedGamesResponseEntity(TypedDict):
    GameID: str
    Title: str
    ImageIcon: str
    ConsoleID: str
    ConsoleName: str
    MaxPossible: str
    NumAwarded: str
    PctWon: str
    HardcoreMode: Literal["0", "1"]


GetUserCompletedGamesResponse = list[UserCompletedGamesResponseEntity]
