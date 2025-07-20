from typing import TypedDict


class GetAchievementTicketStatsResponse(TypedDict):
    achievementId: int
    achievementTitle: str
    achievementDescription: str
    url: str
    openTickets: int
