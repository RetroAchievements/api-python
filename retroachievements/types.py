from enum import Enum
from typing import Literal, TypedDict

AchievementType = Literal["progression", "win_condition", "missable"] | None
AwardKindType = Literal["beaten-softcore", "beaten-hardcore", "completed", "mastered"]
AwardType = Literal[
    "Achievement Points Yield",
    "Achievement Unlocks Yield",
    "Certified Legend",
    "Game Beaten",
    "Invalid or deprecated award type",
    "Mastery/Completion",
    "Patreon Supporter",
]
GameAwardKind = Literal[
    "beaten-softcore",
    "beaten-hardcore",
    "completed",
    "mastered",
]


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
    HighestAwardKind: AwardKindType | None
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
    AuthorULID: str
    DateModified: str
    DateCreated: str
    BadgeName: str
    DisplayOrder: str
    MemAddr: str
    type: AchievementType


class GameExtendedRawAchievementEntityWithUserProgress(
    GameExtendedRawAchievementEntity
):
    DateEarned: str
    DateEarnedHardcore: str


class GameExtendedRawClaimEntity(TypedDict):
    User: str
    SetType: str
    ClaimType: GameExtendedClaimType
    Created: str
    Expiration: str


class GetGameExtendedResponseWithoutClaims(TypedDict):
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


class GetGameExtendedResponse(GetGameExtendedResponseWithoutClaims):
    Claims: list[GameExtendedRawClaimEntity]
    Achievements: dict[int, GameExtendedRawAchievementEntity]
    ReleasedAtGranularity: str
    GuideURL: str | None
    Updated: str
    ParentGameID: int | None
    NumDistinctPlayers: int


class GameHashResult(TypedDict):
    MD5: str
    Name: str
    Labels: list[str]
    PatchUrl: str | None


class GetGameHashesResponse(TypedDict):
    Results: list[GameHashResult]


class GetAchievementCountResponse(TypedDict):
    GameID: int
    AchievementIDs: list[int]


GetAchievementDistributionResponse = dict[str, int]


class RawGameRankAndScoreEntity(TypedDict):
    User: str
    ULID: str
    NumAchievements: int
    TotalScore: int
    LastAward: str


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


class GetRecentGameAwardsEntity(TypedDict):
    User: str
    ULID: str
    AwardKind: AwardKindType
    AwardDate: str
    GameID: int
    GameTitle: str
    ConsoleID: int
    ConsoleName: str


class GetRecentGameAwardsResponse(TypedDict):
    Count: int
    Total: int
    Results: list[GetRecentGameAwardsEntity]


class SetClaimResponseEntity(TypedDict):
    ID: int
    User: str
    ULID: str
    GameID: int
    GameTitle: str
    GameIcon: str
    ConsoleName: str
    ConsoleID: int
    ClaimType: int
    SetType: int
    Status: int
    Extension: int
    Special: int
    Created: str
    DoneTime: str
    Updated: str
    MinutesLeft: int
    UserIsJrDev: Literal[0, 1]


GetSetClaimsResponse = list[SetClaimResponseEntity]


TopTenUsersResponseEntity = TypedDict(
    "TopTenUsersResponseEntity",
    {
        "1": str,  # Username
        "2": str,  # Total points earned by the user
        "3": str,  # Total ratio (white) points earned by the user
        "4": str,  # the user's unique queryable ULID
    },
)


GetTopTenUsersResponse = list[TopTenUsersResponseEntity]


class GetGameInfoAndUserProgressResponse(GetGameExtendedResponseWithoutClaims):
    Achievements: dict[int, GameExtendedRawAchievementEntityWithUserProgress]

    NumAwardedToUser: int
    NumAwardedToUserHardcore: int
    UserCompletion: str
    UserCompletionHardcore: str
    HighestAwardKind: AwardKindType | None
    HighestAwardDate: str | None
    ReleasedAtGranularity: str
    GuideURL: str | None
    ParentGameID: int | None
    NumDistinctPlayers: int
    UserTotalPlaytime: int


class GetUserClaimsResponseEntity(TypedDict):
    ID: str
    User: str
    ULID: str
    GameID: str
    GameTitle: str
    GameIcon: str
    ConsoleID: int
    ConsoleName: str
    ClaimType: str
    SetType: str
    Status: str
    Extension: str
    Special: str
    Created: str
    DoneTime: str
    Updated: str
    UserIsJrDev: int
    MinutesLeft: str


GetUserClaimsResponse = list[GetUserClaimsResponseEntity]


class GetUserGameRankAndScoreResponseEntity(TypedDict):
    User: str
    ULID: str
    UserRank: int
    TotalScore: int
    LastAward: str


GetUserGameRankAndScoreResponse = list[GetUserGameRankAndScoreResponseEntity]


class GetUserPointsResponse(TypedDict):
    Points: int
    SoftcorePoints: int


class UserProgressResponseEntity(TypedDict):
    NumPossibleAchievements: str
    PossibleScore: str
    NumAchieved: int
    ScoreAchieved: int
    NumAchievedHardcore: int
    ScoreAchievedHardcore: int


GetUserProgressResponse = dict[str, UserProgressResponseEntity]


class UserRecentlyPlayedGameResponseEntity(TypedDict):
    GameID: str
    ConsoleID: str
    ConsoleName: str
    Title: str
    ImageIcon: str
    ImageTitle: str
    ImageIngame: str
    ImageBoxArt: str
    AchievementsTotal: int
    LastPlayed: str
    NumPossibleAchievements: int
    PossibleScore: int
    NumAchieved: int
    ScoreAchieved: int
    NumAchievedHardcore: int
    ScoreAchievedHardcore: int


GetUserRecentlyPlayedGamesResponse = list[UserRecentlyPlayedGameResponseEntity]
