from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.cards import assert_issue_virtual_card_response
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.cards.client import CardsGatewayHTTPTestClient
from tests.fixtures.gateway.accounts import DebitCardAccountHTTPFixture
from tests.fixtures.gateway.users import UserHTTPFixture
from tests.schema.cards import IssueVirtualCardRequestTestSchema, IssueVirtualCardResponseTestSchema
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_cards
@pytest.mark.regression
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.CARDS_GATEWAY_SERVICE)
class TestCardsHTTP:
    @allure.story(AllureStory.ISSUE_VIRTUAL_CARD)
    @allure.title("[HTTP] Issue virtual card")
    def test_issue_virtual_card(
            self,
            function_http_user: UserHTTPFixture,
            function_debit_card_account: DebitCardAccountHTTPFixture,
            cards_gateway_http_test_client: CardsGatewayHTTPTestClient
    ):
        request = IssueVirtualCardRequestTestSchema(
            user_id=function_http_user.id,
            account_id=function_debit_card_account.id
        )
        response = cards_gateway_http_test_client.issue_virtual_card_api(request)
        response_data = IssueVirtualCardResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_issue_virtual_card_response(response_data, request)
        validate_json_schema(response.json(), response_data.model_json_schema())

