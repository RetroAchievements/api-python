from typing import TypedDict

from retroachievements.models.get_most_recent_tickets import TicketEntity


class GetGameTicketStatsResponse(TypedDict):
    gameId: int
    gameTitle: str
    consoleName: str
    openTickets: int
    url: str

    tickets: list[TicketEntity]
