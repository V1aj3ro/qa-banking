import pytest

from tests.clients.http.gateway.documents.client import (
    DocumentsGatewayHTTPTestClient,
    build_documents_gateway_http_test_client
)


@pytest.fixture
def documents_gateway_http_test_client() -> DocumentsGatewayHTTPTestClient:
    return build_documents_gateway_http_test_client()


