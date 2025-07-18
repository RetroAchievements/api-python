from enum import Enum
from typing import Literal, TypedDict

AchievementType = Literal["progression", "win_condition", "missable"] | None
AwardKind = Literal["beaten-softcore", "beaten-hardcore", "completed", "mastered"]
AwardType = Literal[
    "Achievement Points Yield",
    "Achievement Unlocks Yield",
    "Certified Legend",
    "Game Beaten",
    "Invalid or deprecated award type",
    "Mastery/Completion",
    "Patreon Supporter",
]


class UserProfileResponse(TypedDict):
    User: str
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


class GetUserRecentAchievementsEntity(TypedDict):
    Date: str
    HardcoreMode: int  # 0 or 1
    AchievementID: int
    Title: str
    Description: str
    BadgeName: str
    Points: int
    Author: str
    GameTitle: str
    GameIcon: str
    GameID: int
    ConsoleName: str
    BadgeURL: str
    GameURL: str


GetUserRecentAchievementsResponse = list[GetUserRecentAchievementsEntity]


class DatedUserAchievementResponseEntity(TypedDict):
    Date: str
    HardcoreMode: str
    AchievementID: str
    Title: str
    Description: str
    BadgeName: str
    Points: str
    Author: str
    GameTitle: str
    GameIcon: str
    GameID: str
    ConsoleName: str
    CumulScore: int
    BadgeURL: str
    GameURL: str
    Type: AchievementType


DatedUserAchievementResponse = list[DatedUserAchievementResponseEntity]


class GetUserCompletionProgressResponseEntity(TypedDict):
    GameID: int
    Title: str
    ImageIcon: str
    ConsoleID: int
    ConsoleName: str
    MaxPossible: int
    NumAwarded: int
    NumAwardedHardcore: int
    MostRecentAwardedDate: str | None
    HighestAwardKind: AwardKind | None
    HighestAwardDate: str | None


class GetUserCompletionProgressResponse(TypedDict):
    Count: int
    Total: int
    Results: list[GetUserCompletionProgressResponseEntity]


class GameExtendedClaimType(Enum):
    Primary = "0"
    Collaboration = "1"


class GameExtendedRawAchievementEntity(TypedDict):
    ID: str
    NumAwarded: str
    NumAwardedHardcore: str
    Title: str
    Description: str
    Points: str
    TrueRatio: str
    Author: str
    DateModified: str
    DateCreated: str
    BadgeName: str
    DisplayOrder: str
    MemAddr: str


class GameExtendedRawClaimEntity(TypedDict):
    User: str
    SetType: str
    ClaimType: GameExtendedClaimType
    Created: str
    Expiration: str


class GetGameExtendedResponse(TypedDict):
    ID: int
    Title: str
    ConsoleID: int
    ForumTopicID: int
    Flags: int
    ImageIcon: str
    ImageTitle: str
    ImageIngame: str
    ImageBoxArt: str
    Publisher: str
    Developer: str
    Genre: str
    Released: str
    IsFinal: bool
    ConsoleName: str
    RichPresencePatch: str
    NumAchievements: int
    NumDistinctPlayersCasual: str
    NumDistinctPlayersHardcore: str
    Claims: list[GameExtendedRawClaimEntity]
    Achievements: dict[int, GameExtendedRawAchievementEntity] | list[int]


class GameHashResult(TypedDict):
    MD5: str
    Name: str
    Labels: list[str]
    PatchUrl: str


class GetGameHashesResponse(TypedDict):
    Results: list[GameHashResult]


class GetAchievementCountResponse(TypedDict):
    GameID: int
    AchievementIDs: list[int]


GetAchievementDistributionResponse = dict[str, int]


class RawGameRankAndScoreEntity(TypedDict):
    User: str
    TotalScore: str
    LastAward: str
    Rank: int


GetGameRankAndScoreResponse = list[RawGameRankAndScoreEntity]


class GetUserAwardsEntity(TypedDict):
    AwardedAt: str
    AwardType: AwardType
    AwardData: int
    AwardDataExtra: int
    DisplayOrder: int
    Title: str
    ConsoleName: str
    Flags: int | None
    ImageIcon: str


class GetUserAwardsResponse(TypedDict):
    TotalAwardsCount: int
    HiddenAwardsCount: int
    MasteryAwardsCount: int
    CompletionAwardsCount: int
    BeatenHardcoreAwardsCount: int
    BeatenSoftcoreAwardsCount: int
    EventAwardsCount: int
    SiteAwardsCount: int
    VisibleUserAwards: list[GetUserAwardsEntity]
