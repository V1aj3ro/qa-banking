import allure

from tests.assertions.base import assert_equal
from tests.assertions.http.errors import assert_validation_error_response
from tests.schema.errors import ValidationErrorSchema, ValidationErrorResponseSchema
from tests.schema.users import (
    UserTestSchema,
    CreateUserRequestTestSchema,
    CreateUserResponseTestSchema,
    GetUserResponseTestSchema
)
from tests.tools.logger import get_test_logger

logger = get_test_logger("USERS_GATEWAY_ASSERTIONS")

@allure.step("Check user")
def assert_user(actual: UserTestSchema, expected: UserTestSchema) -> None:
    logger.info("Check user")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.phone_number, expected.phone_number, "phone_number")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.last_name, expected.last_name, "last_name")

@allure.step("Check create user response")
def assert_create_user_response(request: CreateUserRequestTestSchema, response: CreateUserResponseTestSchema) -> None:
    logger.info("Check create user response")

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
    logger.info("Check get user response")

    assert_user(get_user_response.user, create_user_response.user)

@allure.step("Check get user response with incorrect user id")
def assert_get_user_response_with_incorrect_user_id(actual: ValidationErrorResponseSchema) -> None:
    logger.info("Check get user response with incorrect user id")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=[
                    "path",
                    "user_id"
                ],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-user-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                },
            )
        ]
    )
    assert_validation_error_response(actual, expected)