from typing import Optional

import allure
from httpx import Response

from tests.clients.http.api_coverage import tracker
from tests.clients.http.client import HTTPTestClient
from tests.clients.http.gateway.client import build_gateway_http_test_client
from tests.context.base import RequestContext
from tests.schema.users import CreateUserRequestTestSchema, GetUserResponseTestSchema, CreateUserResponseTestSchema
from tests.tools.fakers import fake
from tests.tools.logger import get_test_logger
from tests.tools.routes import APITestRoutes


class UsersGatewayHTTPTestClient(HTTPTestClient):
    @allure.step("Get user")
    @tracker.track_coverage_httpx(f"{APITestRoutes.USERS}/{{user_id}}")
    def get_user_api(self, user_id: str, context: Optional[RequestContext] = None) -> Response:
        return self.get(
            f"{APITestRoutes.USERS}/{user_id}",
            context=context
        )

    @allure.step("Create user")
    @tracker.track_coverage_httpx(APITestRoutes.USERS)
    def create_user_api(
            self,
            request: CreateUserRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(APITestRoutes.USERS, json=request.model_dump(by_alias=True), context=context)

    def get_user(
            self,
            user_id: Optional[str],
            context: Optional[RequestContext] = None
    ) -> GetUserResponseTestSchema:
        if user_id is None:
            user_id = fake.uuid()
        response = self.get_user_api(user_id, context)
        return GetUserResponseTestSchema.model_validate_json(response.text)

    def create_user(
            self,
            request: Optional[CreateUserRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> CreateUserResponseTestSchema:
        if request is None:
            request=CreateUserRequestTestSchema()
        response = self.create_user_api(request, context)
        return CreateUserResponseTestSchema.model_validate_json(response.text)


def build_users_gateway_http_test_client() -> UsersGatewayHTTPTestClient:
    return UsersGatewayHTTPTestClient(client=build_gateway_http_test_client(
        logger=get_test_logger("USERS_GATEWAY_HTTP_TEST_CLIENT")
        )
    )