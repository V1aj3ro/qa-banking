import pytest

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest
from tests.clients.grpc.gateway.users.client import UsersGatewayGRPCTestClient, build_users_gateway_grpc_test_client
from tests.fixtures.grpc.gateway.users.schema import UserGRPCFixture
from tests.tools.fakers import fake


@pytest.fixture
def users_gateway_grpc_test_client() -> UsersGatewayGRPCTestClient:
    return build_users_gateway_grpc_test_client()

@pytest.fixture
def function_grpc_user(users_gateway_grpc_test_client: UsersGatewayGRPCTestClient) -> UserGRPCFixture:
    request = CreateUserRequest(
        email=str(fake.email()),
        last_name=fake.last_name(),
        first_name=fake.first_name(),
        middle_name=fake.middle_name(),
        phone_number=fake.phone_number()
    )
    response = users_gateway_grpc_test_client.create_user_api(request)
    return UserGRPCFixture(request=request, response=response)