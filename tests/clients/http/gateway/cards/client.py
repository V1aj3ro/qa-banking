from typing import Optional

import allure
from httpx import Response

from tests.clients.http.api_coverage import tracker
from tests.clients.http.client import HTTPTestClient
from tests.clients.http.gateway.client import build_gateway_http_test_client
from tests.context.base import RequestContext
from tests.schema.cards import (
    IssuePhysicalCardRequestTestSchema,
    IssuePhysicalCardResponseTestSchema,
    IssueVirtualCardRequestTestSchema,
    IssueVirtualCardResponseTestSchema

)
from tests.tools.fakers import fake
from tests.tools.logger import get_test_logger
from tests.tools.routes import APITestRoutes



class CardsGatewayHTTPTestClient(HTTPTestClient):
    @allure.step("Issue virtual card")
    @tracker.track_coverage_httpx(f"{APITestRoutes.CARDS}/issue-virtual-card")
    def issue_virtual_card_api(
        self,
        request: IssueVirtualCardRequestTestSchema,
        context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.CARDS}/issue-virtual-card",
            json=request.model_dump(by_alias=True),
            context=context
        )

    @allure.step("Issue physical card")
    @tracker.track_coverage_httpx(f"{APITestRoutes.CARDS}/issue-physical-card")
    def issue_physical_card_api(
        self,
        request: IssuePhysicalCardRequestTestSchema,
        context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.CARDS}/issue-physical-card",
            json=request.model_dump(by_alias=True),
            context=context
        )

    def issue_virtual_card(
        self,
        request: Optional[IssueVirtualCardRequestTestSchema],
        context: Optional[RequestContext] = None
    ) -> IssueVirtualCardResponseTestSchema:
        if request is None:
            request = IssueVirtualCardRequestTestSchema(user_id=fake.uuid, account_id=fake.uuid())
        response = self.issue_virtual_card_api(request, context)
        return IssueVirtualCardResponseTestSchema.model_validate_json(response.text)

    def issue_physical_card(
        self,
        request: Optional[IssuePhysicalCardRequestTestSchema],
        context: Optional[RequestContext] = None
    ) -> IssuePhysicalCardResponseTestSchema:
        if request is None:
            request = IssuePhysicalCardRequestTestSchema(user_id=fake.uuid, account_id=fake.uuid())
        response = self.issue_physical_card_api(request, context)
        return IssuePhysicalCardResponseTestSchema.model_validate_json(response.text)


def build_cards_gateway_http_test_client() -> CardsGatewayHTTPTestClient:
    return CardsGatewayHTTPTestClient(client=build_gateway_http_test_client(
        logger=get_test_logger("CARDS_GATEWAY_HTTP_TEST_CLIENT")
        )
    )

