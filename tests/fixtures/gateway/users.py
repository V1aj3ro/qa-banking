import pytest
from pydantic import BaseModel, EmailStr

from tests.clients.http.gateway.users.client import UsersGatewayHTTPTestClient, build_users_gateway_http_test_client
from tests.schema.users import CreateUserResponseTestSchema, CreateUserRequestTestSchema


class UserHTTPFixture(BaseModel):
    request: CreateUserRequestTestSchema
    response: CreateUserResponseTestSchema


    @property
    def id(self) -> str:
        return self.response.user.id



@pytest.fixture
def users_gateway_http_test_client() -> UsersGatewayHTTPTestClient:
    return build_users_gateway_http_test_client()

@pytest.fixture
def function_http_user(users_gateway_http_test_client: UsersGatewayHTTPTestClient) -> UserHTTPFixture:
    request = CreateUserRequestTestSchema()
    response = users_gateway_http_test_client.create_user(request)
    return UserHTTPFixture(request=request, response=response)