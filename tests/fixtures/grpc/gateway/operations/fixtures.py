import pytest

from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import MakeFeeOperationRequest
from tests.clients.grpc.gateway.operations.client import (
    OperationsGatewayGRPCTestClient,
    build_operations_gateway_grpc_test_client
)
from tests.fixtures.grpc.gateway.accounts.schema import CreditCardAccountGRPCFixture
from tests.fixtures.grpc.gateway.operations.schema import FeeOperationGRPCFixture


@pytest.fixture
def operations_gateway_grpc_test_client() -> OperationsGatewayGRPCTestClient:
    return build_operations_gateway_grpc_test_client()

@pytest.fixture
def function_fee_grpc_operation(
        operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient,
        function_credit_card_grpc_account: CreditCardAccountGRPCFixture
) -> FeeOperationGRPCFixture:
    request = MakeFeeOperationRequest(
        account_id=str(function_credit_card_grpc_account.id),
        card_id=str(function_credit_card_grpc_account.response.account.cards[0].id)
    )
    response = operations_gateway_grpc_test_client.make_fee_operation(
        account_id=str(request.account_id),
        card_id=str(request.card_id)
    )
    return FeeOperationGRPCFixture(request=request, response=response)