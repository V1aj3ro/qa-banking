from logging import Logger
from typing import Any, TypedDict

import allure
from httpx import Client, URL, QueryParams, Response

from tests.clients.http.event_hooks.logger_event_hook import HTTPLoggerEventHook
from tests.tools.config.http import HTTPClientTestConfig



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


def build_http_test_client(
    logger: Logger,
    config: HTTPClientTestConfig
) -> Client:
    logger_event_hook = HTTPLoggerEventHook(logger=logger)

    return Client(
        timeout=config.timeout,
        base_url=str(config.url),
        event_hooks={
            "request": [logger_event_hook.request],
            "response": [logger_event_hook.response],
        },
    )

