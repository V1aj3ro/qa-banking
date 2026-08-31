import logging

from httpx import Client

from tests.clients.http.event_hooks.logger_event_hook import HTTPLoggerEventHook
from config import settings


def build_gateway_http_test_client(
    logger: logging.Logger,
) -> Client:
    logger_event_hook = HTTPLoggerEventHook(logger=logger)

    return Client(
        timeout=settings.gateway_http_client.timeout,
        base_url=settings.gateway_http_client.url,
        event_hooks={
            "request": [logger_event_hook.request],
            "response": [logger_event_hook.response],
        },
    )

