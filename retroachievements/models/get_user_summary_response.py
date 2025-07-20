from typing import Literal, TypedDict


class RecentlyPlayedGameEntity(TypedDict):
    GameID: str
    ConsoleID: str
    ConsoleName: str
    Title: str
    ImageIcon: str
    LastPlayed: str


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


class RecentlyAwardedAchievementEntity(TypedDict):
    NumPossibleAchievements: str
    PossibleScore: str
    NumAchieved: int | str
    ScoreAchieved: int | str
    NumAchievedHardcore: int | str
    ScoreAchievedHardcore: int | str


class ExtendedRecentAchievementEntity(TypedDict):
    ID: str
    GameID: str
    GameTitle: str
    Title: str
    Description: str
    Points: str
    BadgeName: str
    IsAwarded: Literal["1"]
    DateAwarded: str
    HardcoreAchieved: Literal["0"]


class GetUserSummaryResponse(TypedDict):
    RecentlyPlayedCount: int
    RecentlyPlayed: list[RecentlyPlayedGameEntity]
    MemberSince: str

    LastActivity: dict[str, str | int]

    RichPresenceMsg: str
    LastGameID: str
    LastGame: LastGameEntity
    ContribCount: str
    ContribYield: str
    TotalPoints: str
    TotalSoftcorePoints: str
    TotalTruePoints: str
    Permissions: str
    Untracked: Literal["0", "1"]
    ID: str
    UserWallActive: Literal["0", "1"]
    Motto: str
    Rank: int
    Awarded: dict[str, RecentlyAwardedAchievementEntity]

    RecentAchievements: dict[str, dict[str, ExtendedRecentAchievementEntity]]

    Points: str
    SoftcorePoints: str
    UserPic: str
    TotalRanked: int
    Status: str
