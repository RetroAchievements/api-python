from typing import TypedDict


class GetDeveloperTicketStatsResponse(TypedDict):
    User: str
    ULID: str
    Open: int
    Closed: int
    Resolved: int
    Total: int
    URL: str
