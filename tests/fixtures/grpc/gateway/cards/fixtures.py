import pytest

from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import IssueVirtualCardRequest
from tests.clients.grpc.gateway.cards.client import CardsGatewayGRPCTestClient, build_cards_gateway_grpc_test_client
from tests.fixtures.grpc.gateway.accounts.schema import DebitCardAccountGRPCFixture
from tests.fixtures.grpc.gateway.cards.schema import VirtualCardGRPCFixture
from tests.fixtures.grpc.gateway.users.schema import UserGRPCFixture


@pytest.fixture
def cards_gateway_grpc_test_client() -> CardsGatewayGRPCTestClient:
    return build_cards_gateway_grpc_test_client()

@pytest.fixture
def function_virtual_grpc_card(
        cards_gateway_grpc_test_client: CardsGatewayGRPCTestClient,
        function_grpc_user: UserGRPCFixture,
        function_debit_card_grpc_account: DebitCardAccountGRPCFixture
) -> VirtualCardGRPCFixture:
    request = IssueVirtualCardRequest(
        user_id=str(function_grpc_user.id),
        account_id=str(function_debit_card_grpc_account.id)
    )
    response = cards_gateway_grpc_test_client.issue_virtual_card(
        account_id = str(request.account_id),
        user_id=str(request.user_id)
    )
    return VirtualCardGRPCFixture(request=request, response=response)