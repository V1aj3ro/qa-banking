import logging

from httpx import Client

from tests.clients.http.event_hooks.logger_event_hook import HTTPLoggerEventHook
from tests.tools.config.http import HTTPClientTestConfig


def build_http_test_client(
    logger: logging.Logger,
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

