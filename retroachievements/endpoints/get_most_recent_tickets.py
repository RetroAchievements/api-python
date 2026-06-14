from typing import TypedDict


class TicketEntity(TypedDict):
    ID: int
    AchievementID: int
    AchievementTitle: str
    AchievementDesc: str
    AchievementType: str | None
    Points: int
    BadgeName: str
    AchievementAuthor: str
    AchievementAuthorULID: str
    GameID: int
    ConsoleName: str
    GameTitle: str
    GameIcon: str
    ReportedAt: str
    ReportType: int
    ReportState: int
    Hardcore: bool | None
    ReportNotes: str
    ReportedBy: str
    ReportedByULID: str
    ResolvedAt: str | None
    ResolvedBy: str | None
    ResolvedByULID: str | None
    ReportStateDescription: str
    ReportTypeDescription: str


class GetMostRecentTicketsResponse(TypedDict):
    RecentTickets: list[TicketEntity]
    OpenTickets: int
    URL: str
