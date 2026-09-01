import allure
from httpx import Response

from tests.clients.http.client import HTTPTestClient
from tests.clients.http.gateway.client import build_gateway_http_test_client
from tests.schema.users import CreateUserRequestTestSchema, GetUserResponseTestSchema, CreateUserResponseTestSchema
from tests.tools.logger import get_test_logger
from tests.tools.routes import APITestRoutes


class UsersGatewayHTTPTestClient(HTTPTestClient):
    @allure.step("Get user")
    def get_user_api(self, user_id: str) -> Response:
        return self.get(
            f"{APITestRoutes.USERS}/{user_id}"
        )

    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestTestSchema) -> Response:
        return self.post(APITestRoutes.USERS, json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseTestSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseTestSchema.model_validate_json(response.text)

    def create_user(self, request: CreateUserRequestTestSchema) -> CreateUserResponseTestSchema:
        response = self.create_user_api(request)
        return CreateUserResponseTestSchema.model_validate_json(response.text)


def build_users_gateway_http_test_client() -> UsersGatewayHTTPTestClient:
    return UsersGatewayHTTPTestClient(client=build_gateway_http_test_client(
        logger=get_test_logger("USERS_GATEWAY_HTTP_TEST_CLIENT")
        )
    )