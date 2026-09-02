import pytest

from tests.clients.grpc.gateway.documents.client import (
    DocumentsGatewayGRPCTestClient,
    build_documents_gateway_grpc_test_client
)


@pytest.fixture
def documents_gateway_grpc_test_client() -> DocumentsGatewayGRPCTestClient:
    return build_documents_gateway_grpc_test_client()


