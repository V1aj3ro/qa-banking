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
from tests.fixtures.grpc.gateway.accounts.schema import CreditCardAccountGRPCFixture
from tests.fixtures.grpc.gateway.users.schema import UserGRPCFixture
from tests.tools.allure import AllureTag, AllureFeature, AllureEpic, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_accounts
@pytest.mark.regression
@pytest.mark.integration
@allure.tag(AllureTag.GRPC, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.ACCOUNTS_GATEWAY_SERVICE)
class TestAccountsGRPC:
    @allure.story(AllureStory.GET_ACCOUNTS)
    @allure.title("[gRPC] Get accounts")
    def test_get_accounts(
            self,
            function_grpc_user: UserGRPCFixture,
            function_credit_card_grpc_account: CreditCardAccountGRPCFixture,
            accounts_gateway_grpc_test_client: AccountsGatewayGRPCTestClient
    ):
        request = GetAccountsRequest(user_id=function_grpc_user.id)
        response = accounts_gateway_grpc_test_client.get_accounts_api(request)

        assert_get_accounts_response(response, [function_credit_card_grpc_account.response.account])



    @allure.story(AllureStory.OPEN_DEPOSIT_ACCOUNT)
    @allure.title("[gRPC] Open deposit account")
    def test_open_deposit_account(
            self,
            function_grpc_user: UserGRPCFixture,
            accounts_gateway_grpc_test_client: AccountsGatewayGRPCTestClient
    ):
        request = OpenDepositAccountRequest(user_id=function_grpc_user.id)
        response = accounts_gateway_grpc_test_client.open_deposit_account_api(request)

        assert_open_deposit_account_response(response, request)


    @allure.story(AllureStory.OPEN_SAVINGS_ACCOUNT)
    @allure.title("[gRPC] Open savings account")
    def test_open_savings_account(
            self,
            function_grpc_user: UserGRPCFixture,
            accounts_gateway_grpc_test_client: AccountsGatewayGRPCTestClient
    ):
        request = OpenSavingsAccountRequest(user_id=function_grpc_user.id)
        response = accounts_gateway_grpc_test_client.open_savings_account_api(request)

        assert_open_savings_account_response(response, request)


    @allure.story(AllureStory.OPEN_DEBIT_CARD_ACCOUNT)
    @allure.title("[gRPC] Open debit card account")
    def test_open_debit_card_account(
            self,
            function_grpc_user: UserGRPCFixture,
            accounts_gateway_grpc_test_client: AccountsGatewayGRPCTestClient
    ):
        request = OpenDebitCardAccountRequest(user_id=function_grpc_user.id)
        response = accounts_gateway_grpc_test_client.open_debit_card_account_api(request)

        assert_open_debit_card_account_response(response, request)


    @allure.story(AllureStory.OPEN_CREDIT_CARD_ACCOUNT)
    @allure.title("[gRPC] Open credit card account")
    def test_open_credit_card_account(
            self,
            function_grpc_user: UserGRPCFixture,
            accounts_gateway_grpc_test_client: AccountsGatewayGRPCTestClient
    ):
        request = OpenCreditCardAccountRequest(user_id=function_grpc_user.id)
        response = accounts_gateway_grpc_test_client.open_credit_card_account_api(request)

        assert_open_credit_card_account_response(response, request)

