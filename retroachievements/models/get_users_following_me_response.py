from typing import TypedDict


class GetUsersFollowingMeResponseEntity(TypedDict):
    User: str
    ULID: str
    Points: int
    PointsSoftcore: int
    AmIFollowing: bool


class GetUsersFollowingMeResponse(TypedDict):
    Count: int
    Total: int
    Results: list[GetUsersFollowingMeResponseEntity]
