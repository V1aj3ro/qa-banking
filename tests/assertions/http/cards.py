import allure

from tests.assertions.base import assert_equal
from tests.assertions.http.errors import assert_validation_error_response
from tests.schema.cards import (
    CardTestSchema,
    IssuePhysicalCardResponseTestSchema,
    IssueVirtualCardRequestTestSchema,
    IssueVirtualCardResponseTestSchema,
    IssuePhysicalCardRequestTestSchema
)
from tests.schema.errors import ValidationErrorResponseSchema, ValidationErrorSchema
from tests.tools.logger import get_test_logger
from tests.types.cards import CardTestType

logger = get_test_logger("CARDS_GATEWAY_ASSERTIONS")

@allure.step("Check card")
def assert_card(actual: CardTestSchema, expected: CardTestSchema):
    logger.info("Check card")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.account_id, expected.account_id, "account_id")
    assert_equal(actual.status, expected.status, "status")
    assert_equal(actual.card_holder, expected.card_holder, "card_holder")
    assert_equal(actual.card_number, expected.card_number, "card_number")
    assert_equal(actual.cvv, expected.cvv, "cvv")
    assert_equal(actual.expiry_date, expected.expiry_date, "expiry_date")
    assert_equal(actual.payment_system, expected.payment_system, "payment_system")
    assert_equal(actual.pin, expected.pin, "pin")
    assert_equal(actual.type, expected.type, "type")

@allure.step("Check issue physical card response")
def assert_issue_physical_card_response(
        issue_physical_card_response: IssuePhysicalCardResponseTestSchema,
        issue_physical_card_request: IssuePhysicalCardRequestTestSchema
) -> None:
    logger.info("Check issue physical card response")

    assert_equal(issue_physical_card_response.card.type, CardTestType.PHYSICAL, "Card type")
    assert_equal(issue_physical_card_response.card.account_id, issue_physical_card_request.account_id, "Account id")

@allure.step("Check issue virtual card response")
def assert_issue_virtual_card_response(
        issue_virtual_card_response: IssueVirtualCardResponseTestSchema,
        issue_virtual_card_request: IssueVirtualCardRequestTestSchema
) -> None:
    logger.info("Check issue virtual card response")

    assert_equal(issue_virtual_card_response.card.type, CardTestType.VIRTUAL, "Card type")
    assert_equal(issue_virtual_card_response.card.account_id, issue_virtual_card_request.account_id, "Account id")

@allure.step("Check issue physical card response with incorrect user id")
def assert_issue_physical_card_response_with_incorrect_user_id(actual: ValidationErrorResponseSchema) -> None:
    logger.info("Check issue physical card response with incorrect user id")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=[
                    "body",
                    "userId"
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

@allure.step("Check issue virtual card response with incorrect user id")
def assert_issue_virtual_card_response_with_incorrect_user_id(actual: ValidationErrorResponseSchema) -> None:
    logger.info("Check issue virtual card response with incorrect user id")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=[
                    "body",
                    "userId"
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

@allure.step("Check issue physical card response with incorrect account id")
def assert_issue_physical_card_response_with_incorrect_account_id(actual: ValidationErrorResponseSchema) -> None:
    logger.info("Check issue physical card response with incorrect account id")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=[
                    "body",
                    "accountId"
                ],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-account-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                },
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Check issue virtual card response with incorrect  account id")
def assert_issue_virtual_card_response_with_incorrect_account_id(actual: ValidationErrorResponseSchema) -> None:
    logger.info("Check issue virtual card response with incorrect account id")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=[
                    "body",
                    "accountId"
                ],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-account-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                },
            )
        ]
    )
    assert_validation_error_response(actual, expected)



@allure.step("Check issue physical card response with incorrect user id and account id")
def assert_issue_physical_card_response_with_incorrect_user_id_and_account_id(actual: ValidationErrorResponseSchema) -> None:
    logger.info("Check issue physical card response with incorrect user id and account id")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=[
                    "body",
                    "userId"
                ],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-user-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
             },
            ),
            ValidationErrorSchema(
                type="uuid_parsing",
                location=[
                    "body",
                    "accountId"
                ],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-account-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                },
            )
        ]
    )
    assert_validation_error_response(actual, expected)

@allure.step("Check issue virtual card response with incorrect user id and account id")
def assert_issue_virtual_card_response_with_incorrect_user_id_and_account_id(actual: ValidationErrorResponseSchema) -> None:
    logger.info("Check issue virtual card response with incorrect user id and account id")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=[
                    "body",
                    "userId"
                ],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-user-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
             },
            ),
            ValidationErrorSchema(
                type="uuid_parsing",
                location=[
                    "body",
                    "accountId"
                ],
                message="Input should be a valid UUID, invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1",
                input="incorrect-account-id",
                context={
                    "error": "invalid character: expected an optional prefix of `urn:uuid:` followed by [0-9a-fA-F-], found `i` at 1"
                },
            )
        ]
    )
    assert_validation_error_response(actual, expected)

