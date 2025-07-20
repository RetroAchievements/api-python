from typing import TypedDict


class TicketEntity(TypedDict):
    id: int
    achievementId: int
    achievementTitle: str
    achievementDesc: str
    points: int
    badgeName: str
    achievementAuthor: str
    gameId: int
    consoleName: str
    gameTitle: str
    gameIcon: str
    reportedAt: str
    reportType: int
    reportState: int
    hardcore: bool | None
    reportNotes: str
    reportedBy: str
    resolvedAt: str | None
    resolvedBy: str | None
    reportStateDescription: str
    reportTypeDescription: str
    url: str


class GetMostRecentTicketsResponse(TypedDict):
    recentTickets: list[TicketEntity]
    openTickets: int
    url: str
