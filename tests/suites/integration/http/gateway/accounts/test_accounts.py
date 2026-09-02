from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.accounts import assert_open_debit_card_account_response
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.accounts.client import AccountsGatewayHTTPTestClient
from tests.fixtures.gateway.users import UserHTTPFixture
from tests.schema.accounts import OpenDebitCardAccountRequestTestSchema, OpenDebitCardAccountResponseTestSchema
from tests.tools.allure import AllureTag, AllureFeature, AllureEpic, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_accounts
@pytest.mark.regression
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.ACCOUNTS_GATEWAY_SERVICE)
class TestAccountsHTTP:
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