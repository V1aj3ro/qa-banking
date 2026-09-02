from pydantic import BaseModel

from tests.schema.users import CreateUserRequestTestSchema, CreateUserResponseTestSchema


class UserHTTPFixture(BaseModel):
    request: CreateUserRequestTestSchema
    response: CreateUserResponseTestSchema


    @property
    def id(self) -> str:
        return self.response.user.id


