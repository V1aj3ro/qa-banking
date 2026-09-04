from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.documents import assert_get_document_response_with_incorrect_account_id
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.documents.client import DocumentsGatewayHTTPTestClient
from tests.schema.errors import ValidationErrorResponseSchema
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_documents
@pytest.mark.regression
@pytest.mark.negative
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE, AllureTag.NEGATIVE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.DOCUMENTS_GATEWAY_SERVICE)
class TestDocumentsNegativeHTTP:
    @allure.story(AllureStory.GET_TARIFF_DOCUMENT)
    @allure.title("[HTTP] Get tariff document with incorrect account id")
    def test_get_tariff_document_with_incorrect_account_id(
            self,
            documents_gateway_http_test_client: DocumentsGatewayHTTPTestClient
    ):
        response = documents_gateway_http_test_client.get_tariff_document_api(
            account_id="incorrect-account-id"
        )
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_document_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_CONTRACT_DOCUMENT)
    @allure.title("[HTTP] Get contract document with incorrect account id")
    def test_get_contract_document_with_incorrect_account_id(
            self,
            documents_gateway_http_test_client: DocumentsGatewayHTTPTestClient
    ):
        response = documents_gateway_http_test_client.get_contract_document_api(
            account_id="incorrect-account-id"
        )
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_document_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())