from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.accounts import assert_open_debit_card_account_response, \
    assert_open_savings_account_response, assert_open_deposit_account_response, \
    assert_open_credit_card_account_response, assert_get_accounts_response
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.accounts.client import AccountsGatewayHTTPTestClient
from tests.fixtures.http.gateway.accounts.schema import CreditCardAccountHTTPFixture
from tests.fixtures.http.gateway.users.schema import UserHTTPFixture
from tests.schema.accounts import OpenDebitCardAccountRequestTestSchema, OpenDebitCardAccountResponseTestSchema, \
    OpenSavingsAccountRequestTestSchema, OpenSavingsAccountResponseTestSchema, OpenDepositAccountResponseTestSchema, \
    OpenDepositAccountRequestTestSchema, OpenCreditCardAccountRequestTestSchema, \
    OpenCreditCardAccountResponseTestSchema, GetAccountsQueryTestSchema, GetAccountsResponseTestSchema
from tests.tools.allure import AllureTag, AllureFeature, AllureEpic, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_accounts
@pytest.mark.regression
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.ACCOUNTS_GATEWAY_SERVICE)
class TestAccountsHTTP:
    @allure.story(AllureStory.GET_ACCOUNTS)
    @allure.title("[HTTP] Get accounts")
    def test_get_accounts(
            self,
            function_http_user: UserHTTPFixture,
            function_credit_card_http_account: CreditCardAccountHTTPFixture,
            accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient
    ):
        query = GetAccountsQueryTestSchema(user_id=function_http_user.id)
        response = accounts_gateway_http_test_client.get_accounts_api(query)
        response_data = GetAccountsResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_accounts_response(response_data, [function_credit_card_http_account.response.account])

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.OPEN_DEPOSIT_ACCOUNT)
    @allure.title("[HTTP] Open deposit account")
    def test_open_deposit_account(
            self,
            function_http_user: UserHTTPFixture,
            accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient
    ):
        request = OpenDepositAccountRequestTestSchema(user_id=function_http_user.id)
        response = accounts_gateway_http_test_client.open_deposit_account_api(request)
        response_data = OpenDepositAccountResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_open_deposit_account_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.OPEN_SAVINGS_ACCOUNT)
    @allure.title("[HTTP] Open savings account")
    def test_open_savings_account(
            self,
            function_http_user: UserHTTPFixture,
            accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient
    ):
        request = OpenSavingsAccountRequestTestSchema(user_id=function_http_user.id)
        response = accounts_gateway_http_test_client.open_savings_account_api(request)
        response_data = OpenSavingsAccountResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_open_savings_account_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.OPEN_DEBIT_CARD_ACCOUNT)
    @allure.title("[HTTP] Open debit card account")
    def test_open_debit_card_account(
            self,
            function_http_user: UserHTTPFixture,
            accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient
    ):
        request = OpenDebitCardAccountRequestTestSchema(user_id=function_http_user.id)
        response = accounts_gateway_http_test_client.open_debit_card_account_api(request)
        response_data = OpenDebitCardAccountResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_open_debit_card_account_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.OPEN_CREDIT_CARD_ACCOUNT)
    @allure.title("[HTTP] Open credit card account")
    def test_open_credit_card_account(
            self,
            function_http_user: UserHTTPFixture,
            accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient
    ):
        request = OpenCreditCardAccountRequestTestSchema(user_id=function_http_user.id)
        response = accounts_gateway_http_test_client.open_credit_card_account_api(request)
        response_data = OpenCreditCardAccountResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_open_credit_card_account_response(response_data, request)

        validate_json_schema(response.json(), response_data.model_json_schema())
