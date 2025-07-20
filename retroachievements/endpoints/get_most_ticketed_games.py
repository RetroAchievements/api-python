from typing import TypedDict


class ReportedGameEntity(TypedDict):
    gameId: int
    gameTitle: str
    gameIcon: str
    console: str
    openTickets: int


class GetMostTicketedGamesResponse(TypedDict):
    mostReportedGames: list[ReportedGameEntity]
    url: str
