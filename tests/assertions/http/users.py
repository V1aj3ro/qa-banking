import allure

from tests.assertions.base import assert_equal
from tests.schema.users import UserTestSchema, CreateUserRequestTestSchema, CreateUserResponseTestSchema, \
    GetUserResponseTestSchema


@allure.step("Check user")
def assert_user(actual: UserTestSchema, expected: UserTestSchema) -> None:
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.phone_number, expected.phone_number, "phone_number")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.last_name, expected.last_name, "last_name")

@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestTestSchema, response: CreateUserResponseTestSchema) -> None:
    assert_equal(request.email, response.user.email, "email")
    assert_equal(request.phone_number, response.user.phone_number, "phone_number")
    assert_equal(request.middle_name, response.user.middle_name, "middle_name")
    assert_equal(request.first_name, response.user.first_name, "first_name")
    assert_equal(request.last_name, response.user.last_name, "last_name")

@allure.step("Check get user response")
def assert_get_user_response(
        get_user_response: GetUserResponseTestSchema,
        create_user_response: CreateUserResponseTestSchema
) -> None:
    assert_user(get_user_response.user, create_user_response.user)