from typing import Optional
from uuid import UUID

import allure
from httpx import Response

from tests.clients.http.api_coverage import tracker
from tests.clients.http.client import HTTPTestClient
from tests.clients.http.gateway.client import (
    build_gateway_http_test_client,
)
from tests.context.base import RequestContext
from tests.schema.documents import (
    GetTariffDocumentResponseTestSchema,
    GetContractDocumentResponseTestSchema
)
from tests.tools.fakers import fake
from tests.tools.logger import get_test_logger
from tests.tools.routes import APITestRoutes

class DocumentsGatewayHTTPTestClient(HTTPTestClient):
    @allure.step("Get tariff document")
    @tracker.track_coverage_httpx(f"{APITestRoutes.DOCUMENTS}/tariff-document/{{account_id}}")
    def get_tariff_document_api(self, account_id: str, context: Optional[RequestContext] = None) -> Response:
        return self.get(
            f"{APITestRoutes.DOCUMENTS}/tariff-document/{account_id}",
            context=context
        )

    @allure.step("Get contract document")
    @tracker.track_coverage_httpx(f"{APITestRoutes.DOCUMENTS}/contract-document/{{account_id}}")
    def get_contract_document_api(self, account_id: str, context: Optional[RequestContext] = None) -> Response:
        return self.get(
            f"{APITestRoutes.DOCUMENTS}/contract-document/{account_id}",
            context=context
        )

    def get_tariff_document(
            self,
            account_id: Optional[str],
            context: Optional[RequestContext] = None
    ) -> GetTariffDocumentResponseTestSchema:
        if account_id is None:
            account_id=fake.uuid()
        response = self.get_tariff_document_api(account_id, context)
        return GetTariffDocumentResponseTestSchema.model_validate_json(response.text)

    def get_contract_document(
            self,
            account_id: Optional[str],
            context: Optional[RequestContext] = None
    ) -> GetContractDocumentResponseTestSchema:
        if account_id is None:
            account_id=fake.uuid()
        response = self.get_contract_document_api(account_id, context)
        return GetContractDocumentResponseTestSchema.model_validate_json(response.text)


def build_documents_gateway_http_test_client() -> DocumentsGatewayHTTPTestClient:
    return DocumentsGatewayHTTPTestClient(client=build_gateway_http_test_client(
        logger=get_test_logger("DOCUMENTS_GATEWAY_HTTP_TEST_CLIENT")
        )
    )