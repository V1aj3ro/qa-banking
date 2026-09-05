from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.cards import (
    assert_issue_physical_card_response_with_incorrect_user_id,
    assert_issue_virtual_card_response_with_incorrect_user_id,
    assert_issue_virtual_card_response_with_incorrect_user_id_and_account_id,
    assert_issue_physical_card_response_with_incorrect_user_id_and_account_id,
    assert_issue_physical_card_response_with_incorrect_account_id,
    assert_issue_virtual_card_response_with_incorrect_account_id
)
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.cards.client import CardsGatewayHTTPTestClient
from tests.fixtures.http.gateway.accounts.schema import DebitCardAccountHTTPFixture
from tests.fixtures.http.gateway.users.schema import UserHTTPFixture
from tests.schema.cards import (
    IssueVirtualCardRequestTestSchema,
    IssuePhysicalCardRequestTestSchema
)
from tests.schema.errors import ValidationErrorResponseSchema
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_cards
@pytest.mark.regression
@pytest.mark.negative
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE, AllureTag.NEGATIVE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.CARDS_GATEWAY_SERVICE)
class TestCardsNegativeHTTP:
    @allure.story(AllureStory.ISSUE_PHYSICAL_CARD)
    @allure.title("[HTTP] Issue virtual card with incorrect user id")
    def test_issue_virtual_card_with_incorrect_user_id(
            self,
            function_debit_card_http_account: DebitCardAccountHTTPFixture,
            cards_gateway_http_test_client: CardsGatewayHTTPTestClient
    ):
        request = IssueVirtualCardRequestTestSchema(
            user_id="incorrect-user-id",
            account_id=function_debit_card_http_account.id
        )
        response = cards_gateway_http_test_client.issue_virtual_card_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_issue_virtual_card_response_with_incorrect_user_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.ISSUE_PHYSICAL_CARD)
    @allure.title("[HTTP] Issue physical card with incorrect user id")
    def test_issue_physical_card_with_incorrect_user_id(
            self,
            function_debit_card_http_account: DebitCardAccountHTTPFixture,
            cards_gateway_http_test_client: CardsGatewayHTTPTestClient
    ):
        request = IssuePhysicalCardRequestTestSchema(
            user_id="incorrect-user-id",
            account_id=function_debit_card_http_account.id
        )
        response = cards_gateway_http_test_client.issue_physical_card_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_issue_physical_card_response_with_incorrect_user_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.ISSUE_PHYSICAL_CARD)
    @allure.title("[HTTP] Issue virtual card with incorrect account id")
    def test_issue_virtual_card_with_incorrect_account_id(
            self,
            function_http_user: UserHTTPFixture,
            cards_gateway_http_test_client: CardsGatewayHTTPTestClient
    ):
        request = IssueVirtualCardRequestTestSchema(
            user_id=function_http_user.id,
            account_id="incorrect-account-id"
        )
        response = cards_gateway_http_test_client.issue_virtual_card_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_issue_virtual_card_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.ISSUE_PHYSICAL_CARD)
    @allure.title("[HTTP] Issue physical card with incorrect account id")
    def test_issue_physical_card_with_incorrect_account_id(
            self,
            function_http_user: UserHTTPFixture,
            cards_gateway_http_test_client: CardsGatewayHTTPTestClient
    ):
        request = IssuePhysicalCardRequestTestSchema(
            user_id=function_http_user.id,
            account_id="incorrect-account-id"
        )
        response = cards_gateway_http_test_client.issue_physical_card_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_issue_physical_card_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.story(AllureStory.ISSUE_PHYSICAL_CARD)
    @allure.title("[HTTP] Issue virtual card with incorrect user id and account id")
    def test_issue_virtual_card_with_incorrect_user_id_and_account_id(
            self,
            cards_gateway_http_test_client: CardsGatewayHTTPTestClient
    ):
        request = IssueVirtualCardRequestTestSchema(
            user_id="incorrect-user-id",
            account_id="incorrect-account-id"
        )
        response = cards_gateway_http_test_client.issue_virtual_card_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_issue_virtual_card_response_with_incorrect_user_id_and_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.ISSUE_PHYSICAL_CARD)
    @allure.title("[HTTP] Issue physical card with incorrect user id and account id")
    def test_issue_physical_card_with_incorrect_user_id_and_account_id(
            self,
            cards_gateway_http_test_client: CardsGatewayHTTPTestClient
    ):
        request = IssuePhysicalCardRequestTestSchema(
            user_id="incorrect-user-id",
            account_id="incorrect-account-id"
        )
        response = cards_gateway_http_test_client.issue_physical_card_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_issue_physical_card_response_with_incorrect_user_id_and_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())





