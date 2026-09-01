import pytest
from pydantic import BaseModel

from tests.clients.http.gateway.accounts.client import AccountsGatewayHTTPTestClient, \
    build_accounts_gateway_http_test_client
from tests.fixtures.gateway.users import UserHTTPFixture
from tests.schema.accounts import (
    OpenDebitCardAccountRequestTestSchema,
    AccountTestSchema,
    OpenDebitCardAccountResponseTestSchema,
    OpenCreditCardAccountRequestTestSchema,
    OpenCreditCardAccountResponseTestSchema,
    OpenDepositAccountRequestTestSchema,
    OpenDepositAccountResponseTestSchema,
    OpenSavingsAccountRequestTestSchema,
    OpenSavingsAccountResponseTestSchema
)



class DebitCardAccountHTTPFixture(BaseModel):
    request: OpenDebitCardAccountRequestTestSchema
    response: OpenDebitCardAccountResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.account.id


class CreditCardAccountHTTPFixture(BaseModel):
    request: OpenCreditCardAccountRequestTestSchema
    response: OpenCreditCardAccountResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.account.id


class DepositAccountHTTPFixture(BaseModel):
    request: OpenDepositAccountRequestTestSchema
    response: OpenDepositAccountResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.account.id


class SavingsAccountHTTPFixture(BaseModel):
    request: OpenSavingsAccountRequestTestSchema
    response: OpenSavingsAccountResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.account.id



@pytest.fixture
def accounts_gateway_http_test_client() -> AccountsGatewayHTTPTestClient:
    return build_accounts_gateway_http_test_client()

@pytest.fixture()
def function_debit_card_account(
        accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient,
        function_user: UserHTTPFixture
) -> DebitCardAccountHTTPFixture:
    request = OpenDebitCardAccountRequestTestSchema(user_id=function_user.id)
    response = accounts_gateway_http_test_client.open_debit_card_account(request)
    return DebitCardAccountHTTPFixture(request=request, response=response)

@pytest.fixture()
def function_credit_card_account(
        accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient,
        function_user: UserHTTPFixture
) -> CreditCardAccountHTTPFixture:
    request = OpenCreditCardAccountRequestTestSchema(user_id=function_user.id)
    response = accounts_gateway_http_test_client.open_credit_card_account(request)
    return CreditCardAccountHTTPFixture(request=request, response=response)

@pytest.fixture()
def function_deposit_account(
        accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient,
        function_user: UserHTTPFixture
) -> DepositAccountHTTPFixture:
    request = OpenDepositAccountRequestTestSchema(user_id=function_user.id)
    response = accounts_gateway_http_test_client.open_deposit_account(request)
    return DepositAccountHTTPFixture(request=request, response=response)

@pytest.fixture()
def function_savings_account(
        accounts_gateway_http_test_client: AccountsGatewayHTTPTestClient,
        function_user: UserHTTPFixture
) -> SavingsAccountHTTPFixture:
    request = OpenSavingsAccountRequestTestSchema(user_id=function_user.id)
    response = accounts_gateway_http_test_client.open_savings_account(request)
    return SavingsAccountHTTPFixture(request=request, response=response)

