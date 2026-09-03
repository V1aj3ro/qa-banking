from pydantic import BaseModel, Field, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel

from tests.tools.fakers import fake


class UserTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class GetUserResponseTestSchema(BaseModel):
    user: UserTestSchema


class CreateUserRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    email: EmailStr = Field(default_factory = fake.email)
    last_name: str = Field(default_factory = fake.last_name)
    first_name: str = Field(default_factory = fake.first_name)
    middle_name: str = Field(default_factory = fake.middle_name)
    phone_number: str = Field(default_factory = fake.phone_number)


class CreateUserResponseTestSchema(BaseModel):
    user: UserTestSchema


