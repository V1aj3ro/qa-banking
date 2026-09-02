import allure
from grpc import Channel

from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import (
    IssuePhysicalCardRequest,
    IssuePhysicalCardResponse
)
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import (
    IssueVirtualCardRequest,
    IssueVirtualCardResponse
)
from tests.clients.grpc.client import GRPCTestClient
from tests.clients.grpc.gateway.client import build_gateway_grpc_test_client
from tests.tools.logger import get_test_logger


class CardsGatewayGRPCTestClient(GRPCTestClient):
    def __init__(self, channel: Channel):
        super().__init__(channel)

        self.stub = CardsGatewayServiceStub(channel)

    @allure.step("Issue virtual card")
    def issue_virtual_card_api(self, request: IssueVirtualCardRequest) -> IssueVirtualCardResponse:
        return self.stub.IssueVirtualCard(request)

    @allure.step("Issue physical card")
    def issue_physical_card_api(self, request: IssuePhysicalCardRequest) -> IssuePhysicalCardResponse:
        return self.stub.IssuePhysicalCard(request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponse:
        request = IssueVirtualCardRequest(user_id=user_id, account_id=account_id)
        return self.issue_virtual_card_api(request)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponse:
        request = IssuePhysicalCardRequest(user_id=user_id, account_id=account_id)
        return self.issue_physical_card_api(request)


def build_cards_gateway_grpc_test_client() -> CardsGatewayGRPCTestClient:
    return CardsGatewayGRPCTestClient(channel=build_gateway_grpc_test_client(
        logger=get_test_logger("CARDS_GATEWAY_GRPC_TEST_CLIENT")
        )
    )

