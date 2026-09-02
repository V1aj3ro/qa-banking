import pytest

from tests.clients.http.gateway.accounts.client import (
    AccountsGatewayHTTPTestClient,
    build_accounts_gateway_http_test_client
)
from tests.fixtures.http.gateway.accounts.schema import (
    DebitCardAccountHTTPFixture,
    CreditCardAccountHTTPFixture,
    DepositAccountHTTPFixture,
    SavingsAccountHTTPFixture
)
from tests.fixtures.http.gateway.users.fixtures import UserHTTPFixture
from tests.schema.accounts import (
    OpenDebitCardAccountRequestTestSchema,
    OpenCreditCardAccountRequestTestSchema,
    OpenDepositAccountRequestTestSchema,
    OpenSavingsAccountRequestTestSchema
)


@pytest.fixture
def accounts_gateway_http_test_client() -> AccountsGatewayHTTPTestClient:
    return build_accounts_gateway_http_test_client()

@pytest.fixture
def function_debit_card_http_account(
        accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient,
        function_http_user: UserHTTPFixture
) -> DebitCardAccountHTTPFixture:
    request = OpenDebitCardAccountRequestTestSchema(user_id=function_http_user.id)
    response = accounts_gateway_http_test_client.open_debit_card_account(request)
    return DebitCardAccountHTTPFixture(request=request, response=response)

@pytest.fixture
def function_credit_card_http_account(
        accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient,
        function_http_user: UserHTTPFixture
) -> CreditCardAccountHTTPFixture:
    request = OpenCreditCardAccountRequestTestSchema(user_id=function_http_user.id)
    response = accounts_gateway_http_test_client.open_credit_card_account(request)
    return CreditCardAccountHTTPFixture(request=request, response=response)

@pytest.fixture
def function_deposit_http_account(
        accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient,
        function_http_user: UserHTTPFixture
) -> DepositAccountHTTPFixture:
    request = OpenDepositAccountRequestTestSchema(user_id=function_http_user.id)
    response = accounts_gateway_http_test_client.open_deposit_account(request)
    return DepositAccountHTTPFixture(request=request, response=response)

@pytest.fixture
def function_savings_http_account(
        accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient,
        function_http_user: UserHTTPFixture
) -> SavingsAccountHTTPFixture:
    request = OpenSavingsAccountRequestTestSchema(user_id=function_http_user.id)
    response = accounts_gateway_http_test_client.open_savings_account(request)
    return SavingsAccountHTTPFixture(request=request, response=response)

