import allure
from httpx import Response

from tests.clients.http.client import HTTPTestClient
from tests.clients.http.gateway.client import build_gateway_http_test_client
from tests.schema.cards import (
    IssuePhysicalCardRequestTestSchema,
    IssuePhysicalCardResponseTestSchema,
    IssueVirtualCardRequestTestSchema,
    IssueVirtualCardResponseTestSchema

)
from tests.tools.logger import get_test_logger
from tests.tools.routes import APITestRoutes


class CardsGatewayHTTPTestClient(HTTPTestClient):
    @allure.step("Issue virtual card")
    def issue_virtual_card_api(self, request: IssueVirtualCardRequestTestSchema) -> Response:
        return self.post(
            f"{APITestRoutes.CARDS}/issue-virtual-card",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Issue physical card")
    def issue_physical_card_api(self, request: IssuePhysicalCardRequestTestSchema) -> Response:
        return self.post(
            f"{APITestRoutes.CARDS}/issue-physical-card",
            json=request.model_dump(by_alias=True)
        )

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseTestSchema:
        request = IssueVirtualCardRequestTestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_virtual_card_api(request)
        return IssueVirtualCardResponseTestSchema.model_validate_json(response.text)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseTestSchema:
        request = IssuePhysicalCardRequestTestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(request)
        return IssuePhysicalCardResponseTestSchema.model_validate_json(response.text)


def build_cards_gateway_http_test_client() -> CardsGatewayHTTPTestClient:
    return CardsGatewayHTTPTestClient(client=build_gateway_http_test_client(
        logger=get_test_logger("CARDS_GATEWAY_HTTP_TEST_CLIENT")
        )
    )

