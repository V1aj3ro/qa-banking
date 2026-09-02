import allure

from tests.assertions.base import assert_equal
from tests.schema.documents import DocumentTestSchema, GetTariffDocumentResponseTestSchema
from tests.tools.logger import get_test_logger

logger = get_test_logger("DOCUMENTS_GATEWAY_ASSERTIONS")

@allure.step("Check document")
def assert_document(actual: DocumentTestSchema, expected: DocumentTestSchema) -> None:
    logger.info("Check document")

    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")


