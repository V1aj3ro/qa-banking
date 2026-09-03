from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.documents.client import DocumentsGatewayHTTPTestClient
from tests.fixtures.http.gateway.accounts.schema import CreditCardAccountHTTPFixture
from tests.schema.documents import GetTariffDocumentResponseTestSchema, GetContractDocumentResponseTestSchema
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_documents
@pytest.mark.regression
@pytest.mark.integration
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.DOCUMENTS_GATEWAY_SERVICE)
class TestDocumentsHTTP:
    @allure.story(AllureStory.GET_TARIFF_DOCUMENT)
    @allure.title("[HTTP] Get tariff document")
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

    @allure.story(AllureStory.GET_CONTRACT_DOCUMENT)
    @allure.title("[HTTP] Get contract document")
    def test_get_contract_document(
            self,
            function_credit_card_http_account: CreditCardAccountHTTPFixture,
            documents_gateway_http_test_client: DocumentsGatewayHTTPTestClient
    ):
        response = documents_gateway_http_test_client.get_contract_document_api(
            account_id=function_credit_card_http_account.id
        )
        response_data = GetContractDocumentResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        validate_json_schema(response.json(), response_data.model_json_schema())