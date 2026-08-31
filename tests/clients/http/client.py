from typing import Any

import allure
from httpx import Client, URL, QueryParams, Response


class HTTPTestClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Male GET request to {url}")
    def get(
            self,
            url: URL | str,
            params: QueryParams| None = None,
    ) -> Response:
        return self.client.get(url, params=params)

    @allure.step("Make POST request to {url}")
    def post(self,
             url: URL | str,
             json: Any | None = None,
        ) -> Response:
        return self.client.post(url, json=json)



