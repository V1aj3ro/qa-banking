import allure

from tests.assertions.base import assert_equal
from tests.schema.documents import DocumentTestSchema, GetTariffDocumentResponseTestSchema


@allure.step("Check document")
def assert_document(actual: DocumentTestSchema, expected: DocumentTestSchema) -> None:
    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")


