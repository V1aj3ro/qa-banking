import allure
import pytest

from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import IssuePhysicalCardRequest
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import IssueVirtualCardRequest
from tests.assertions.base import assert_status_code
from tests.assertions.grpc.cards import assert_issue_virtual_card_response, assert_issue_physical_card_response
from tests.clients.grpc.gateway.cards.client import CardsGatewayGRPCTestClient
from tests.fixtures.grpc.gateway.accounts.schema import DebitCardAccountGRPCFixture
from tests.fixtures.grpc.gateway.users.schema import UserGRPCFixture
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_cards
@pytest.mark.regression
@allure.tag(AllureTag.GRPC, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.CARDS_GATEWAY_SERVICE)
class TestCardsGRPC:
    @allure.story(AllureStory.ISSUE_VIRTUAL_CARD)
    @allure.title("[gRPC] Issue virtual card")
    def test_issue_virtual_card(
            self,
            function_grpc_user: UserGRPCFixture,
            function_debit_card_grpc_account: DebitCardAccountGRPCFixture,
            cards_gateway_grpc_test_client: CardsGatewayGRPCTestClient
    ):
        request = IssueVirtualCardRequest(
            user_id=function_grpc_user.id,
            account_id=function_debit_card_grpc_account.id
        )
        response = cards_gateway_grpc_test_client.issue_virtual_card_api(request)

        assert_issue_virtual_card_response(response, request)

    @allure.story(AllureStory.ISSUE_PHYSICAL_CARD)
    @allure.title("[gRPC] Issue physical card")
    def test_issue_physical_card(
            self,
            function_grpc_user: UserGRPCFixture,
            function_debit_card_grpc_account: DebitCardAccountGRPCFixture,
            cards_gateway_grpc_test_client: CardsGatewayGRPCTestClient
    ):
        request = IssuePhysicalCardRequest(
            user_id=function_grpc_user.id,
            account_id=function_debit_card_grpc_account.id
        )
        response = cards_gateway_grpc_test_client.issue_physical_card_api(request)

        assert_issue_physical_card_response(response, request)
