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


# {
#   "LastActivity": {
#     "ID": 0,
#     "timestamp": null,
#     "lastupdate": null,
#     "activitytype": null,
#     "User": "xelnia",
#     "data": null,
#     "data2": null
#   },
#   "RichPresenceMsg": "L=08-1 | 1 lives | 189300 points",
#   "RichPresenceMsgDate": "2025-11-19 12:05:04",
#   "LastGameID": 15758,
#   "ContribCount": 0,
#   "ContribYield": 0,
#   "TotalPoints": 8317,
#   "TotalSoftcorePoints": 0,
#   "TotalTruePoints": 26760,
#   "Permissions": 1,
#   "Untracked": 0,
#   "ID": 224958,
#   "UserWallActive": 1,
#   "Motto": "",
#   "Rank": 4616,
#   "RecentlyPlayedCount": 1,
#   "RecentlyPlayed": [
#     {
#       "GameID": 15758,
#       "ConsoleID": 27,
#       "ConsoleName": "Arcade",
#       "Title": "Crazy Kong",
#       "ImageIcon": "/Images/068578.png",
#       "ImageTitle": "/Images/068579.png",
#       "ImageIngame": "/Images/068580.png",
#       "ImageBoxArt": "/Images/068205.png",
#       "LastPlayed": "2023-03-09 08:20:34",
#       "AchievementsTotal": 43
#     }
#   ],
#   "Awarded": {
#     "15758": {
#       "NumPossibleAchievements": 43,
#       "PossibleScore": 615,
#       "NumAchieved": 41,
#       "ScoreAchieved": 490,
#       "NumAchievedHardcore": 41,
#       "ScoreAchievedHardcore": 490
#     }
#   },
#   "RecentAchievements": {
#     "15758": {
#       "293505": {
#         "ID": 293505,
#         "GameID": 15758,
#         "GameTitle": "Crazy Kong",
#         "Title": "Prodigy of the Arcade",
#         "Description": "Score 200,000 points",
#         "Points": 25,
#         "Type": null,
#         "BadgeName": "325551",
#         "IsAwarded": "1",
#         "DateAwarded": "2023-03-09 08:20:34",
#         "HardcoreAchieved": 1
#       },
#       "293526": {
#         "ID": 293526,
#         "GameID": 15758,
#         "GameTitle": "Crazy Kong",
#         "Title": "Super Smasher III",
#         "Description": "Get 6 smashes with a single bottom hammer on any barrel board",
#         "Points": 10,
#         "Type": null,
#         "BadgeName": "325572",
#         "IsAwarded": "1",
#         "DateAwarded": "2023-03-09 08:19:37",
#         "HardcoreAchieved": 1
#       }
#     }
#   },
#   "LastGame": {
#     "ID": 15758,
#     "Title": "Crazy Kong",
#     "ConsoleID": 27,
#     "ConsoleName": "Arcade",
#     "ForumTopicID": 20415,
#     "Flags": 0,
#     "ImageIcon": "/Images/068578.png",
#     "ImageTitle": "/Images/068579.png",
#     "ImageIngame": "/Images/068580.png",
#     "ImageBoxArt": "/Images/068205.png",
#     "Publisher": "Falcon",
#     "Developer": "Falcon",
#     "Genre": "2D Platforming, Arcade",
#     "Released": "1981-01-01",
#     "ReleasedAtGranularity": "year",
#     "IsFinal": 0
#   },
#   "UserPic": "/UserPic/xelnia.png",
#   "TotalRanked": 45654,
#   "Status": "Offline"
# }
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
