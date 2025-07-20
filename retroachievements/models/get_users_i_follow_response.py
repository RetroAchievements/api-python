from typing import TypedDict


class GetUsersIFollowResponseEntity(TypedDict):
    User: str
    ULID: str
    Points: int
    PointsSoftcore: int
    IsFollowingMe: bool


class GetUsersIFollowResponse(TypedDict):
    Count: int
    Total: int
    Results: list[GetUsersIFollowResponseEntity]
