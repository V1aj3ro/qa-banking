from typing import Optional

import allure
from grpc import Channel

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest, GetUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from tests.clients.grpc.client import GRPCTestClient
from tests.clients.grpc.gateway.client import build_gateway_grpc_test_client
from tests.context.base import RequestContext, build_grpc_test_metadata
from tests.tools.fakers import fake
from tests.tools.logger import get_test_logger


class UsersGatewayGRPCTestClient(GRPCTestClient):
    def __init__(self, channel: Channel):
        super().__init__(channel)

        self.stub = UsersGatewayServiceStub(channel)

    @allure.step("Get user")
    def get_user_api(self, request: GetUserRequest, context: Optional[RequestContext] = None) -> GetUserResponse:
        return self.stub.GetUser(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequest, context: Optional[RequestContext] = None) -> CreateUserResponse:
        return self.stub.CreateUser(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    def get_user(self, user_id: Optional[str] = None, context: Optional[RequestContext] = None) -> GetUserResponse:
        if user_id is None:
            user_id = str(fake.uuid())
        request = GetUserRequest(id=user_id)
        return self.get_user_api(request, context)

    def create_user(self, context: Optional[RequestContext] = None) -> CreateUserResponse:
        request = CreateUserRequest(
            email=fake.email(),
            last_name=fake.last_name(),
            first_name=fake.first_name(),
            middle_name=fake.middle_name(),
            phone_number=fake.phone_number()
        )
        return self.create_user_api(request, context)


def build_users_gateway_grpc_test_client() -> UsersGatewayGRPCTestClient:
    return UsersGatewayGRPCTestClient(channel=build_gateway_grpc_test_client(
        logger=get_test_logger("USERS_GATEWAY_GRPC_TEST_CLIENT")
        )
    )

