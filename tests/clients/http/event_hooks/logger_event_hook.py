from logging import Logger

import allure
from httpx import Request, Response

from tests.tools.http.curl import make_curl_from_request


class HTTPLoggerEventHook:
    def __init__(self, logger: Logger):
        self.logger = logger

    def curl_event_hook(request: Request):
        curl_command = make_curl_from_request(request)

        allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)

    def request(self, request: Request):
        self.logger.info(
            f"{request.method} {request.url} - Waiting for response"
        )

    def response(self, response: Response):
        request = response.request
        self.logger.info(
            f"{request.method} {request.url} - Status {response.status_code}"
        )
