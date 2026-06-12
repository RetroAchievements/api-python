from typing import Literal, TypedDict


class RecentlyPlayedGameEntity(TypedDict):
    GameID: str
    ConsoleID: int
    ConsoleName: str
    Title: str
    ImageIcon: str
    ImageTitle: str
    ImageIngame: str
    ImageBoxArt: str
    LastPlayed: str
    AchievementsTotal: int


class LastGameEntity(TypedDict):
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
    ReleasedAtGranularity: str


class LastActivityEntity(TypedDict):
    ID: str
    timestamp: str
    lastupdate: str
    activitytype: str
    User: str
    data: str
    data2: str


class RecentlyAwardedAchievementEntity(TypedDict):
    NumPossibleAchievements: int
    PossibleScore: int
    NumAchieved: int
    ScoreAchieved: int
    NumAchievedHardcore: int
    ScoreAchievedHardcore: int


class ExtendedRecentAchievementEntity(TypedDict):
    ID: int
    GameID: int
    GameTitle: str
    Title: str
    Description: str
    Points: int
    Type: str | None
    BadgeName: str
    IsAwarded: str
    DateAwarded: str
    HardcoreAchieved: int


class GetUserSummaryResponse(TypedDict):
    User: str
    ULID: str
    RichPresenceMsgDate: str
    RecentlyPlayedCount: int
    RecentlyPlayed: list[RecentlyPlayedGameEntity]
    MemberSince: str

    LastActivity: LastActivityEntity

    RichPresenceMsg: str
    LastGameID: str
    LastGame: LastGameEntity
    ContribCount: int
    ContribYield: int
    TotalPoints: int
    TotalSoftcorePoints: int
    TotalTruePoints: int
    Permissions: int
    Untracked: Literal[0, 1]
    ID: int
    UserWallActive: Literal[0, 1]
    Motto: str
    Rank: int
    Awarded: dict[str, RecentlyAwardedAchievementEntity]

    RecentAchievements: dict[str, dict[str, ExtendedRecentAchievementEntity]]

    Points: str
    SoftcorePoints: str
    UserPic: str
    TotalRanked: int
    Status: str
