import pytest

from tests.clients.http.gateway.operations.client import (
    OperationsGatewayHTTPTestClient,
    build_operations_gateway_http_test_client
)
from tests.fixtures.http.gateway.accounts.schema import CreditCardAccountHTTPFixture
from tests.fixtures.http.gateway.operations.schema import FeeOperationHTTPFixture
from tests.schema.operations import MakeFeeOperationRequestTestSchema


@pytest.fixture
def operations_gateway_http_test_client() -> OperationsGatewayHTTPTestClient:
    return build_operations_gateway_http_test_client()

@pytest.fixture
def function_fee_http_operation(
        operations_gateway_http_test_client: OperationsGatewayHTTPTestClient,
        function_credit_card_http_account: CreditCardAccountHTTPFixture
) -> FeeOperationHTTPFixture:
    request = MakeFeeOperationRequestTestSchema(
        account_id=function_credit_card_http_account.id,
        card_id=function_credit_card_http_account.response.account.cards[0].id
    )
    response = operations_gateway_http_test_client.make_fee_operation(request)
    return FeeOperationHTTPFixture(request=request, response=response)