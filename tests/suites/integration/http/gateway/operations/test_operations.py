from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.accounts import assert_open_debit_card_account_response
from tests.assertions.http.operations import assert_make_fee_operation_response
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.accounts.client import AccountsGatewayHTTPTestClient
from tests.clients.http.gateway.operations.client import OperationsGatewayHTTPTestClient
from tests.fixtures.gateway.accounts import DepositAccountHTTPFixture
from tests.fixtures.gateway.cards import VirtualCardHTTPFixture
from tests.fixtures.gateway.users import UserHTTPFixture
from tests.schema.accounts import OpenDebitCardAccountRequestTestSchema, OpenDebitCardAccountResponseTestSchema
from tests.schema.operations import MakeFeeOperationRequestTestSchema, MakeFeeOperationResponseTestSchema
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_operations
@pytest.mark.regression
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.OPERATIONS_GATEWAY_SERVICE)
class TestOperationsHTTP:
    @allure.story(AllureStory.MAKE_FEE_OPERATION)
    @allure.title("[HTTP] Make fee operation")
    def test_make_fee_operation(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeFeeOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_fee_operation_api(request)
        response_data = MakeFeeOperationResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_make_fee_operation_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
