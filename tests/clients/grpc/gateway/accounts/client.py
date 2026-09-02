import allure
from grpc import Channel

from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import GetAccountsRequest, GetAccountsResponse
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountRequest,
    OpenCreditCardAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import (
    OpenDepositAccountRequest,
    OpenDepositAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import (
    OpenSavingsAccountRequest,
    OpenSavingsAccountResponse
)
from tests.clients.grpc.client import GRPCTestClient
from tests.clients.grpc.gateway.client import build_gateway_grpc_test_client
from tests.tools.logger import get_test_logger


class AccountsGatewayGRPCTestClient(GRPCTestClient):
    def __init__(self, channel: Channel):
        super().__init__(channel)

        self.stub = AccountsGatewayServiceStub(channel)

    @allure.step("Get accounts")
    def get_accounts_api(self, request: GetAccountsRequest) -> GetAccountsResponse:
        return self.stub.GetAccounts(request)

    @allure.step("Open deposit account")
    def open_deposit_account_api(self, request: OpenDepositAccountRequest) -> OpenDepositAccountResponse:
        return self.stub.OpenDepositAccount(request)

    @allure.step("Open savings account")
    def open_savings_account_api(self, request: OpenSavingsAccountRequest) -> OpenSavingsAccountResponse:
        return self.stub.OpenSavingsAccount(request)

    @allure.step("Open debit card account")
    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequest) -> OpenDebitCardAccountResponse:
        return self.stub.OpenDebitCardAccount(request)

    @allure.step("Open credit card account")
    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequest) -> OpenCreditCardAccountResponse:
        return self.stub.OpenCreditCardAccount(request)

    def get_accounts(self, user_id: str) -> GetAccountsResponse:
        request = GetAccountsRequest(user_id=user_id)
        return self.get_accounts_api(request)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponse:
        request = OpenDepositAccountRequest(user_id=user_id)
        return self.open_deposit_account_api(request)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponse:
        request = OpenSavingsAccountRequest(user_id=user_id)
        return self.open_savings_account_api(request)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponse:
        request = OpenDebitCardAccountRequest(user_id=user_id)
        return self.open_debit_card_account_api(request)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponse:
        request = OpenCreditCardAccountRequest(user_id=user_id)
        return self.open_credit_card_account_api(request)


def build_accounts_gateway_grpc_test_client() -> AccountsGatewayGRPCTestClient:
    return AccountsGatewayGRPCTestClient(channel=build_gateway_grpc_test_client(
        logger=get_test_logger("ACCOUNTS_GATEWAY_GRPC_TEST_CLIENT")
        )
    )

