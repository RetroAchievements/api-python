from typing import TypedDict


class GetAchievementTicketStatsResponse(TypedDict):
    AchievementId: int
    AchievementTitle: str
    AchievementDescription: str
    AchievementType: str
    URL: str
    OpenTickets: int
