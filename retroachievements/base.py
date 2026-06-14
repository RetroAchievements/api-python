import requests

from retroachievements import __version__

_BASE_URL = "https://retroachievements.org/API/"


class BaseRAClient:
    """
    Main class for accessing the RetroAchievements Web API
    """

    headers = {"User-Agent": "RetroAchievements-api-python/" + __version__}

    def __init__(self, api_key: str):
        self.api_key = api_key

    def url_params(self, params: dict[str, str | int | None] | None = None):
        """
        Inserts the auth and query params into the request
        """
        if params is None:
            params = {}
        params.update({"y": self.api_key})
        return params

    # URL construction
    def call_api(
        self,
        endpoint: str | None = None,
        params: dict[str, str | int | None] | None = None,
        timeout: int = 30,
        headers: dict[str, str] | None = None,
    ):
        if endpoint is None:
            endpoint = ""
        req = requests.get(
            f"{_BASE_URL}{endpoint}",
            params=self.url_params(params),
            timeout=timeout,
            headers=self.headers | (headers or {}),
        )
        return req
