import allure
import pytest

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest
from tests.assertions.grpc.users import assert_create_user_response, assert_get_user_response
from tests.clients.grpc.gateway.users.client import UsersGatewayGRPCTestClient
from tests.fixtures.grpc.gateway.users.schema import UserGRPCFixture
from tests.tools.allure import AllureTag, AllureStory, AllureFeature, AllureEpic
from tests.tools.fakers import fake


@pytest.mark.gateway
@pytest.mark.gateway_users
@pytest.mark.regression
@pytest.mark.integration
@allure.tag(AllureTag.GRPC, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.USERS_GATEWAY_SERVICE)
class TestUsersGRPC:
    @allure.story(AllureStory.CREATE_USER)
    @allure.title("[gRPC] Create user")
    def test_create_user(
            self,
            users_gateway_grpc_test_client: UsersGatewayGRPCTestClient
    ):
        request = CreateUserRequest(
            email=fake.email(),
            last_name=fake.last_name(),
            first_name=fake.first_name(),
            middle_name=fake.middle_name(),
            phone_number=fake.phone_number()
        )
        response = users_gateway_grpc_test_client.create_user_api(request)

        assert_create_user_response(request, response)

    @allure.story(AllureStory.GET_USER)
    @allure.title("[gRPC] Get user")
    def test_get_user(self, function_grpc_user: UserGRPCFixture, users_gateway_grpc_test_client: UsersGatewayGRPCTestClient):
        response = users_gateway_grpc_test_client.get_user(function_grpc_user.id)
        assert_get_user_response(response, function_grpc_user.response)

