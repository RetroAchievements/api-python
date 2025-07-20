from typing import TypedDict


class CommentEntity(TypedDict):
    User: str
    ULID: str
    Submitted: str
    CommentText: str


class GetCommentsResponse(TypedDict):
    Count: int
    Total: int
    Results: list[CommentEntity]
