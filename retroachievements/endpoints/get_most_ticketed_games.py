from typing import TypedDict


class ReportedGameEntity(TypedDict):
    GameID: int
    GameTitle: str
    GameIcon: str
    Console: str
    OpenTickets: int


class GetMostTicketedGamesResponse(TypedDict):
    MostReportedGames: list[ReportedGameEntity]
    URL: str
