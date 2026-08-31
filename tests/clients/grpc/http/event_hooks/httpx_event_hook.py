import allure
from httpx import Request, Response

from tests.tools.http.curl import make_curl_from_request
from tests.tools.logger import get_test_logger

logger = get_test_logger("HTTP_LOGGER")

def curl_event_hook(request: Request):

    curl_command = make_curl_from_request(request)

    allure.attach(curl_command, "cURL command", allure.attachment_type.TEXT)


def log_request_event_hook(request: Request):
    logger.info(f"Make {request.method} request to {request.url}")


def log_response_event_hook(response: Response):
    logger.info(
        f"Got response {response.status_code} {response.reason_phrase} from {response.url}"
    )
