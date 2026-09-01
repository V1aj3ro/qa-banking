from http import HTTPStatus

import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.documents.client import DocumentsGatewayHTTPTestClient
from tests.fixtures.gateway.accounts import CreditCardAccountHTTPFixture
from tests.schema.documents import GetTariffDocumentResponseTestSchema


@pytest.mark.regression
class TestDocumentsHTTP:
    def test_get_tariff_document(
            self,
            function_credit_card_http_account: CreditCardAccountHTTPFixture,
            documents_gateway_http_test_client: DocumentsGatewayHTTPTestClient
    ):
        response = documents_gateway_http_test_client.get_tariff_document_api(
            account_id=function_credit_card_http_account.id
        )
        response_data = GetTariffDocumentResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())