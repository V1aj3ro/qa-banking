import pytest
from pydantic import BaseModel

from tests.clients.http.gateway.operations.client import (
    OperationsGatewayHTTPTestClient,
    build_operations_gateway_http_test_client
)
from tests.fixtures.gateway.accounts import CreditCardAccountFixture
from tests.schema.operations import MakeFeeOperationRequestTestSchema, MakeFeeOperationResponseTestSchema


class FeeOperationHTTPFixture(BaseModel):
    request: MakeFeeOperationRequestTestSchema
    response: MakeFeeOperationResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.operation.id



@pytest.fixture
def operations_gateway_http_test_client() -> OperationsGatewayHTTPTestClient:
    return build_operations_gateway_http_test_client()

@pytest.fixture
def function_fee_http_operation(
        operations_gateway_http_test_client: OperationsGatewayHTTPTestClient,
        function_credit_card_account: CreditCardAccountFixture
) -> FeeOperationHTTPFixture:
    request = MakeFeeOperationRequestTestSchema(
        account_id=function_credit_card_account.id,
        card_id=function_credit_card_account.response.account.cards[0].id
    )
    response = operations_gateway_http_test_client.make_fee_operation(request)
    return FeeOperationHTTPFixture(request=request, response=response)