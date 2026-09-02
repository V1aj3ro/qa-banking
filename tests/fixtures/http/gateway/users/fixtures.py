import pytest

from tests.clients.http.gateway.users.client import UsersGatewayHTTPTestClient, build_users_gateway_http_test_client
from tests.fixtures.http.gateway.users.schema import UserHTTPFixture
from tests.schema.users import CreateUserRequestTestSchema


@pytest.fixture
def users_gateway_http_test_client() -> UsersGatewayHTTPTestClient:
    return build_users_gateway_http_test_client()

@pytest.fixture
def function_http_user(users_gateway_http_test_client: UsersGatewayHTTPTestClient) -> UserHTTPFixture:
    request = CreateUserRequestTestSchema()
    response = users_gateway_http_test_client.create_user(request)
    return UserHTTPFixture(request=request, response=response)