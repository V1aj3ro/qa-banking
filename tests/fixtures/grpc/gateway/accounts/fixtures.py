import pytest

from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import OpenCreditCardAccountRequest
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import OpenDepositAccountRequest
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import OpenSavingsAccountRequest
from tests.clients.grpc.gateway.accounts.client import (
    AccountsGatewayGRPCTestClient,
    build_accounts_gateway_grpc_test_client
)
from tests.fixtures.grpc.gateway.accounts.schema import (
    DebitCardAccountGRPCFixture,
    CreditCardAccountGRPCFixture,
    DepositAccountGRPCFixture,
    SavingsAccountGRPCFixture
)
from tests.fixtures.grpc.gateway.users.fixtures import UserGRPCFixture



@pytest.fixture
def accounts_gateway_grpc_test_client() -> AccountsGatewayGRPCTestClient:
    return build_accounts_gateway_grpc_test_client()

@pytest.fixture
def function_debit_card_grpc_account(
        accounts_gateway_grpc_test_client: AccountsGatewayGRPCTestClient,
        function_grpc_user: UserGRPCFixture
) -> DebitCardAccountGRPCFixture:
    request = OpenDebitCardAccountRequest(user_id=str(function_grpc_user.id))
    response = accounts_gateway_grpc_test_client.open_debit_card_account(request.user_id)
    return DebitCardAccountGRPCFixture(request=request, response=response)

@pytest.fixture
def function_credit_card_grpc_account(
        accounts_gateway_grpc_test_client: AccountsGatewayGRPCTestClient,
        function_grpc_user: UserGRPCFixture
) -> CreditCardAccountGRPCFixture:
    request = OpenCreditCardAccountRequest(user_id=str(function_grpc_user.id))
    response = accounts_gateway_grpc_test_client.open_credit_card_account(request.user_id)
    return CreditCardAccountGRPCFixture(request=request, response=response)

@pytest.fixture
def function_deposit_grpc_account(
        accounts_gateway_grpc_test_client: AccountsGatewayGRPCTestClient,
        function_grpc_user: UserGRPCFixture
) -> DepositAccountGRPCFixture:
    request = OpenDepositAccountRequest(user_id=str(function_grpc_user.id))
    response = accounts_gateway_grpc_test_client.open_deposit_account(request.user_id)
    return DepositAccountGRPCFixture(request=request, response=response)

@pytest.fixture
def function_savings_grpc_account(
        accounts_gateway_grpc_test_client: AccountsGatewayGRPCTestClient,
        function_grpc_user: UserGRPCFixture
) -> SavingsAccountGRPCFixture:
    request = OpenSavingsAccountRequest(user_id=str(function_grpc_user.id))
    response = accounts_gateway_grpc_test_client.open_savings_account(request.user_id)
    return SavingsAccountGRPCFixture(request=request, response=response)

