from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.accounts import (
    assert_get_accounts_response_with_incorrect_user_id,
    assert_open_account_response_with_incorrect_user_id
)
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.accounts.client import AccountsGatewayHTTPTestClient
from tests.schema.accounts import (
    OpenDebitCardAccountRequestTestSchema,
    OpenSavingsAccountRequestTestSchema,
    OpenDepositAccountRequestTestSchema,
    OpenCreditCardAccountRequestTestSchema,
    GetAccountsQueryTestSchema
)
from tests.schema.errors import ValidationErrorResponseSchema
from tests.tools.allure import AllureTag, AllureFeature, AllureEpic, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_accounts
@pytest.mark.regression
@pytest.mark.negative
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE, AllureTag.NEGATIVE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.ACCOUNTS_GATEWAY_SERVICE)
class TestAccountsNegativeHTTP:
    @allure.story(AllureStory.GET_ACCOUNTS)
    @allure.title("[HTTP] Get accounts with incorrect user id")
    def test_get_accounts(
            self,
            accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient
    ):
        query = GetAccountsQueryTestSchema(user_id="incorrect-user-id")
        response = accounts_gateway_http_test_client.get_accounts_api(query)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_accounts_response_with_incorrect_user_id(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.OPEN_DEPOSIT_ACCOUNT)
    @allure.title("[HTTP] Open deposit account with incorrect user id")
    def test_open_deposit_account_with_incorrect_user_id(
            self,
            accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient
    ):
        request = OpenDepositAccountRequestTestSchema(user_id="incorrect-user-id")
        response = accounts_gateway_http_test_client.open_deposit_account_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_open_account_response_with_incorrect_user_id(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.OPEN_SAVINGS_ACCOUNT)
    @allure.title("[HTTP] Open savings account with incorrect user id")
    def test_open_savings_account_with_incorrect_user_id(
            self,
            accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient
    ):
        request = OpenSavingsAccountRequestTestSchema(user_id="incorrect-user-id")
        response = accounts_gateway_http_test_client.open_savings_account_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_open_account_response_with_incorrect_user_id(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.OPEN_DEBIT_CARD_ACCOUNT)
    @allure.title("[HTTP] Open debit card account with incorrect user id")
    def test_open_debit_card_account_with_incorrect_user_id(
            self,
            accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient
    ):
        request = OpenDebitCardAccountRequestTestSchema(user_id="incorrect-user-id")
        response = accounts_gateway_http_test_client.open_debit_card_account_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_open_account_response_with_incorrect_user_id(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.OPEN_CREDIT_CARD_ACCOUNT)
    @allure.title("[HTTP] Open credit card account with incorrect user id")
    def test_open_credit_card_account_with_incorrect_user_id(
            self,
            accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient
    ):
        request = OpenCreditCardAccountRequestTestSchema(user_id="incorrect-user-id")
        response = accounts_gateway_http_test_client.open_credit_card_account_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_open_account_response_with_incorrect_user_id(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
