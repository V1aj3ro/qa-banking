from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.cards import assert_issue_virtual_card_response, assert_issue_physical_card_response
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.cards.client import CardsGatewayHTTPTestClient
from tests.fixtures.http.gateway.accounts.schema import DebitCardAccountHTTPFixture
from tests.fixtures.http.gateway.users.schema import UserHTTPFixture
from tests.schema.cards import (
    IssueVirtualCardRequestTestSchema,
    IssueVirtualCardResponseTestSchema,
    IssuePhysicalCardRequestTestSchema,
    IssuePhysicalCardResponseTestSchema
)
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_cards
@pytest.mark.regression
@pytest.mark.positive
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE, AllureTag.POSITIVE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.CARDS_GATEWAY_SERVICE)
class TestCardsPositiveHTTP:
    @allure.story(AllureStory.ISSUE_VIRTUAL_CARD)
    @allure.title("[HTTP] Issue virtual card")
    def test_issue_virtual_card(
            self,
            function_http_user: UserHTTPFixture,
            function_debit_card_http_account: DebitCardAccountHTTPFixture,
            cards_gateway_http_test_client: CardsGatewayHTTPTestClient
    ):
        request = IssueVirtualCardRequestTestSchema(
            user_id=function_http_user.id,
            account_id=function_debit_card_http_account.id
        )
        response = cards_gateway_http_test_client.issue_virtual_card_api(request)
        response_data = IssueVirtualCardResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_issue_virtual_card_response(response_data, request)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.ISSUE_PHYSICAL_CARD)
    @allure.title("[HTTP] Issue physical card")
    def test_issue_physical_card(
            self,
            function_http_user: UserHTTPFixture,
            function_debit_card_http_account: DebitCardAccountHTTPFixture,
            cards_gateway_http_test_client: CardsGatewayHTTPTestClient
    ):
        request = IssuePhysicalCardRequestTestSchema(
            user_id=function_http_user.id,
            account_id=function_debit_card_http_account.id
        )
        response = cards_gateway_http_test_client.issue_physical_card_api(request)
        response_data = IssuePhysicalCardResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_issue_physical_card_response(response_data, request)
        validate_json_schema(response.json(), response_data.model_json_schema())
