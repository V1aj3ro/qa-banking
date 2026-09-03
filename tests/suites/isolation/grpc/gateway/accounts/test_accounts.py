import allure
import pytest

from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import GetAccountsRequest
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import OpenCreditCardAccountRequest
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import OpenDepositAccountRequest
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import OpenSavingsAccountRequest
from tests.assertions.grpc.accounts import (
    assert_open_debit_card_account_response,
    assert_open_savings_account_response,
    assert_open_deposit_account_response,
    assert_open_credit_card_account_response,
    assert_get_accounts_response
)
from tests.clients.grpc.gateway.accounts.client import AccountsGatewayGRPCTestClient
from tests.context.base import RequestContext
from tests.context.scenario import Scenario
from tests.fixtures.grpc.gateway.accounts.schema import CreditCardAccountGRPCFixture
from tests.fixtures.grpc.gateway.users.schema import UserGRPCFixture
from tests.tools.allure import AllureTag, AllureFeature, AllureEpic, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_accounts
@pytest.mark.regression
@pytest.mark.isolation
@allure.tag(AllureTag.GRPC, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.ACCOUNTS_GATEWAY_SERVICE)
class TestAccountsGRPC:
    @allure.story(AllureStory.GET_ACCOUNTS)
    @allure.title("[gRPC] Get accounts")
    def test_get_accounts(
            self,
            accounts_gateway_grpc_test_client: AccountsGatewayGRPCTestClient
    ):
        response = accounts_gateway_grpc_test_client.get_accounts(
            context = RequestContext(scenario=Scenario.USER_WITH_ACTIVE_DEBIT_CARD_ACCOUNT)
        )


