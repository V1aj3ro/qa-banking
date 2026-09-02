import allure

from contracts.services.documents.contracts.contract_pb2 import Contract
from contracts.services.documents.receipts.receipt_pb2 import Receipt
from contracts.services.documents.tariffs.tariff_pb2 import Tariff
from tests.assertions.base import assert_equal
from tests.tools.logger import get_test_logger

logger = get_test_logger("DOCUMENTS_GATEWAY_ASSERTIONS")

@allure.step("Check document")
def assert_tariff_document(actual: Tariff, expected: Tariff) -> None:
    logger.info("Check tariff document")

    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")

def assert_contract_document(actual: Contract, expected: Contract) -> None:
    logger.info("Check contract document")

    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")

def assert_receipt_document(actual: Receipt, expected: Receipt) -> None:
    logger.info("Check receipt document")

    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")
