from typing import TypedDict


class GetGameTicketStatsResponse(TypedDict):
    GameId: int
    GameTitle: str
    ConsoleName: str
    OpenTickets: int
    URL: str
