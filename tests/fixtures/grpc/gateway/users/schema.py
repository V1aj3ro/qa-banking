from pydantic import BaseModel, ConfigDict

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse


class UserGRPCFixture(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: CreateUserRequest
    response: CreateUserResponse


    @property
    def id(self) -> str:
        return self.response.user.id


