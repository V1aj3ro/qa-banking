import allure

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse, CreateUserRequest
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserResponse
from contracts.services.users.user_pb2 import User
from tests.assertions.base import assert_equal
from tests.tools.logger import get_test_logger

logger = get_test_logger("USERS_GATEWAY_ASSERTIONS")

@allure.step("Check user")
def assert_user(actual: User, expected: User) -> None:
    logger.info("Check user")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.phone_number, expected.phone_number, "phone_number")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.last_name, expected.last_name, "last_name")


@allure.step("Check create user response")
def assert_create_user_response(actual: CreateUserResponse, expected: CreateUserResponse) -> None:
    logger.info("Check create user response")

    assert_user(actual.user, expected.user)

@allure.step("Check get user response")
def assert_get_user_response(
        actual: GetUserResponse,
        expected: GetUserResponse
) -> None:
    logger.info("Check get user response")

    assert_user(actual.user, expected.user)

@allure.step("Check create user response. User with active debit card account")
def assert_create_user_response_user_with_active_debit_card_account(actual: CreateUserResponse) -> None:
    logger.info("Check create user response. User with active debit card account")

    expected = CreateUserResponse(
        user=User(
            id="2d412ec4-52a5-41c1-885e-65acffb1f42f",
            email="Gomes.Anton@company.com",
            lastName="Gomes",
            firstName="Anton",
            middleName="Jerald",
            phoneNumber="+1-212-456-7890",
       )
    )

    assert_create_user_response(actual, expected)

@allure.step("Check get user response. User with active debit card account")
def assert_create_user_response_user_with_active_debit_card_account(actual: GetUserResponse) -> None:
    logger.info("Check get user response. User with active debit card account")

    expected = GetUserResponse(
        user=User(
            id="2d412ec4-52a5-41c1-885e-65acffb1f42f",
            email="Gomes.Anton@company.com",
            lastName="Gomes",
            firstName="Anton",
            middleName="Jerald",
            phoneNumber="+1-212-456-7890",
       )
    )

    assert_get_user_response(actual, expected)


@allure.step("Check create user response. User with one purchase and one top up operation")
def assert_create_user_response_user_with_one_purchase_and_one_top_up_operations(actual: CreateUserResponse) -> None:
    logger.info("Check create user response. User with one purchase and one top up operation")

    expected = CreateUserResponse(
        user=User(
            id="2d412ec4-52a5-41c1-885e-65acffb1f42f",
            email="Gomes.Anton@company.com",
            lastName="Gomes",
            firstName="Anton",
            middleName="Jerald",
            phoneNumber="+1-212-456-7890",
       )
    )

    assert_create_user_response(actual, expected)

@allure.step("Check get user response. User with one purchase and one top up operation")
def assert_create_user_response_user_with_one_purchase_and_one_top_up_operations(actual: GetUserResponse) -> None:
    logger.info("Check get user response. User with one purchase and one top up operation")

    expected = GetUserResponse(
        user=User(
            id="2d412ec4-52a5-41c1-885e-65acffb1f42f",
            email="Gomes.Anton@company.com",
            lastName="Gomes",
            firstName="Anton",
            middleName="Jerald",
            phoneNumber="+1-212-456-7890",
       )
    )

    assert_get_user_response(actual, expected)