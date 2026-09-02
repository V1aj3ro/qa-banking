import pytest

from tests.clients.http.gateway.cards.client import CardsGatewayHTTPTestClient, build_cards_gateway_http_test_client
from tests.fixtures.http.gateway.accounts.schema import DebitCardAccountHTTPFixture
from tests.fixtures.http.gateway.cards.schema import VirtualCardHTTPFixture
from tests.fixtures.http.gateway.users.schema import UserHTTPFixture
from tests.schema.cards import IssueVirtualCardRequestTestSchema


@pytest.fixture
def cards_gateway_http_test_client() -> CardsGatewayHTTPTestClient:
    return build_cards_gateway_http_test_client()

@pytest.fixture
def function_virtual_http_card(
        cards_gateway_http_test_client: CardsGatewayHTTPTestClient,
        function_http_user: UserHTTPFixture,
        function_debit_card_http_account: DebitCardAccountHTTPFixture
) -> VirtualCardHTTPFixture:
    request = IssueVirtualCardRequestTestSchema(
        user_id=function_http_user.id,
        account_id=function_debit_card_http_account.id
    )
    response = cards_gateway_http_test_client.issue_virtual_card(request)
    return VirtualCardHTTPFixture(request=request, response=response)