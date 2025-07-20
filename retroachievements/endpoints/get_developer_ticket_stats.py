from typing import TypedDict


class GetDeveloperTicketStatsResponse(TypedDict):
    user: str
    open: int
    closed: int
    resolved: int
    total: int
    url: str
