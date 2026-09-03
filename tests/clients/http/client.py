from typing import Any

import allure
from httpx import Client, URL, QueryParams, Response, Headers

from tests.context.base import RequestContext, build_http_test_headers


class HTTPTestClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Male GET request to {url}")
    def get(
            self,
            url: URL | str,
            params: QueryParams| None = None,
            context: RequestContext | None = None
    ) -> Response:
        headers = Headers()

        if context:
            headers = Headers(build_http_test_headers(context))

        return self.client.get(url, params=params, headers=headers)

    @allure.step("Make POST request to {url}")
    def post(self,
             url: URL | str,
             json: Any | None = None,
             context: RequestContext | None = None
        ) -> Response:
        headers = Headers()

        if context:
            headers = Headers(build_http_test_headers(context))


        return self.client.post(url, json=json, headers=headers)



