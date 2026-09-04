import allure

from tests.assertions.base import assert_equal
from tests.assertions.http.errors import assert_validation_error_response
from tests.schema.documents import DocumentTestSchema
from tests.schema.errors import ValidationErrorResponseSchema, ValidationErrorSchema
from tests.tools.logger import get_test_logger

logger = get_test_logger("DOCUMENTS_GATEWAY_ASSERTIONS")

@allure.step("Check document")
def assert_document(actual: DocumentTestSchema, expected: DocumentTestSchema) -> None:
    logger.info("Check document")

    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")


@allure.step("Check get document response with incorrect account id")
def assert_get_document_response_with_incorrect_account_id(actual: ValidationErrorResponseSchema) -> None:
    logger.info("Check get document response with incorrect account id")
    expected = ValidationErrorResponseSchema(
        detail=[
            ValidationErrorSchema(
                type="uuid_parsing",
                location=[
                    "path",
                    "account_id"
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

