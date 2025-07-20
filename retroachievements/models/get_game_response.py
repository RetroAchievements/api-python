from typing import TypedDict


class GetGameResponse(TypedDict):
    ID: int
    Title: str
    ForumTopicID: int
    ConsoleID: int
    ConsoleName: str
    Flags: int
    ImageIcon: str
    GameIcon: str
    ImageTitle: str
    ImageIngame: str
    ImageBoxArt: str
    Publisher: str
    Developer: str
    Genre: str
    Released: str
    GameTitle: str
    Console: str
