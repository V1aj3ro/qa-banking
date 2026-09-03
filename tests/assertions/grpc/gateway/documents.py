import allure

from contracts.services.documents.contracts.contract_pb2 import Contract
from contracts.services.documents.receipts.receipt_pb2 import Receipt
from contracts.services.documents.tariffs.tariff_pb2 import Tariff
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import GetContractDocumentResponse
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import GetTariffDocumentResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import GetOperationReceiptResponse
from tests.assertions.base import assert_equal
from tests.tools.logger import get_test_logger

logger = get_test_logger("DOCUMENTS_GATEWAY_ASSERTIONS")

@allure.step("Check tariff document")
def assert_tariff_document(actual: Tariff, expected: Tariff) -> None:
    logger.info("Check tariff document")

    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")

@allure.step("Check contract document")
def assert_contract_document(actual: Contract, expected: Contract) -> None:
    logger.info("Check contract document")

    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")

@allure.step("Check receipt document")
def assert_receipt_document(actual: Receipt, expected: Receipt) -> None:
    logger.info("Check receipt document")

    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")

@allure.step("Check get tariff document response")
def assert_get_tariff_document_response(actual: GetTariffDocumentResponse, expected: GetTariffDocumentResponse) -> None:
    logger.info("Check get tariff document response")

    assert_tariff_document(actual.tariff, expected.tariff)

@allure.step("Check get contract document response")
def assert_get_contract_document_response(actual: GetContractDocumentResponse, expected: GetContractDocumentResponse) -> None:
    logger.info("Check get tariff document response")

    assert_contract_document(actual.contract, expected.contract)

@allure.step("Check get receipt document response")
def assert_get_operation_receipt_response(actual: GetOperationReceiptResponse, expected: GetOperationReceiptResponse) -> None:
    logger.info("Check get receipt document response")

    assert_receipt_document(actual.receipt, expected.receipt)

@allure.step("Check get tariff document response. User with active debit card account")
def assert_get_tariff_document_response_user_with_active_debit_card_account(actual: GetTariffDocumentResponse) -> None:
    logger.info("Check get tariff document response. User with active debit card account")
    expected = GetTariffDocumentResponse(Tariff(
        url="http://localhost:3000/tariff/document.pdf",
        document="dGFyaWZmLWRvY3VtZW50"
    ))
    
    assert_get_tariff_document_response(actual, expected)


@allure.step("Check get contract document response. User with active debit card account")
def assert_get_contract_document_response_user_with_active_debit_card_account(actual: GetContractDocumentResponse) -> None:
    logger.info("Check get contract document response. User with active debit card account")
    expected = GetContractDocumentResponse(
        Contract(
            url="http://localhost:3000/contract/document.pdf",
            document="Y29udHJhY3QtZG9jdW1lbnQ="
        )
    )

    assert_get_contract_document_response(actual, expected)


@allure.step("Check get tariff document response. User with one purchase and one top up operations")
def assert_get_tariff_document_response_user_with_one_purchase_and_one_top_up_operations(actual: GetTariffDocumentResponse) -> None:
    logger.info("Check get tariff document response. User with one purchase and one top up operations")
    expected = GetTariffDocumentResponse(
        Tariff(
            url="http://localhost:3000/tariff/document.pdf",
            document="dGFyaWZmLWRvY3VtZW50"
        )
    )

    assert_get_tariff_document_response(actual, expected)

@allure.step("Check get contract document response. User with one purchase and one top up operations")
def assert_get_contract_document_response_user_with_one_purchase_and_one_top_up_operations(actual: GetContractDocumentResponse) -> None:
    logger.info("Check get contract document response. User with one purchase and one top up operations")
    expected = GetContractDocumentResponse(
        Contract(
            url="http://localhost:3000/contract/document.pdf",
            document="Y29udHJhY3QtZG9jdW1lbnQ="
        )
    )

    assert_get_contract_document_response(actual, expected)
    
@allure.step("Check get operation receipt document response. User with one purchase and one top up operations")
def assert_get_operation_receipt_document_response_user_with_one_purchase_and_one_top_up_operations(actual: GetOperationReceiptResponse) -> None:
    logger.info("Check get operation receipt document response. User with one purchase and one top up operations")
    expected = GetOperationReceiptResponse(
        Receipt(
            url="http://localhost:3000/receipt/document.pdf",
            document="cmVjZWlwdC1kb2N1bWVudA"
        )
    )

    assert_get_operation_receipt_response(actual, expected)

