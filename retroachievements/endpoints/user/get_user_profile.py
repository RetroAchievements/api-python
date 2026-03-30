from typing import TypedDict

from retroachievements.base import BaseRAClient


class UserProfileResponse(TypedDict):
    User: str
    ULID: str
    UserPic: str
    MemberSince: str
    RichPresenceMsg: str
    LastGameID: int
    ContribCount: int
    ContribYield: int
    TotalPoints: int
    TotalSoftcorePoints: int
    TotalTruePoints: int
    Permissions: int
    Untracked: int
    ID: int
    UserWallActive: int
    Motto: str


def get_user_profile(self: BaseRAClient, username: str) -> UserProfileResponse:
    """
    A call to this method will retrieve summary information about a given user,
    targeted by username.

    Params:
        username (str): The target username or ULID.
    """
    result = self.call_api("API_GetUserProfile.php?", {"u": username}).json()
    return result
