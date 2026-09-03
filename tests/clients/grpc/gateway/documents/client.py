from typing import Optional

import allure
from grpc import Channel

from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import (
    GetContractDocumentRequest,
    GetContractDocumentResponse
)
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import (
    GetTariffDocumentRequest,
    GetTariffDocumentResponse
)
from tests.clients.grpc.client import GRPCTestClient
from tests.clients.grpc.gateway.client import build_gateway_grpc_test_client
from tests.context.base import RequestContext, build_grpc_test_metadata
from tests.tools.fakers import fake
from tests.tools.logger import get_test_logger


class DocumentsGatewayGRPCTestClient(GRPCTestClient):
    def __init__(self, channel: Channel):
        super().__init__(channel)

        self.stub = DocumentsGatewayServiceStub(channel)

    @allure.step("Get tariff document")
    def get_tariff_document_api(
            self,
            request: GetTariffDocumentRequest,
            context: Optional[RequestContext] = None
    ) -> GetTariffDocumentResponse:
        return self.stub.GetTariffDocument(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Get contract document")
    def get_contract_document_api(
            self,
            request: GetContractDocumentRequest,
            context: Optional[RequestContext] = None
    ) -> GetContractDocumentResponse:
        return self.stub.GetContractDocument(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    def get_tariff_document(
            self,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> GetTariffDocumentResponse:
        if account_id is None:
            account_id = str(fake.uuid())
        request = GetTariffDocumentRequest(account_id=account_id)
        return self.get_tariff_document_api(request, context)

    def get_contract_document(
            self,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> GetContractDocumentResponse:
        if account_id is None:
            account_id = str(fake.uuid())
        request = GetContractDocumentRequest(account_id=account_id)
        return self.get_contract_document_api(request, context)


def build_documents_gateway_grpc_test_client() -> DocumentsGatewayGRPCTestClient:
    return DocumentsGatewayGRPCTestClient(channel=build_gateway_grpc_test_client(
        logger=get_test_logger("DOCUMENTS_GATEWAY_GRPC_TEST_CLIENT")
        )
    )

