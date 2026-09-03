import allure

from contracts.services.documents.contracts.contract_pb2 import Contract
from contracts.services.documents.receipts.receipt_pb2 import Receipt
from contracts.services.documents.tariffs.tariff_pb2 import Tariff
from tests.assertions.base import assert_equal
from tests.schema.documents import TariffTestSchema, ContractTestSchema, GetTariffDocumentResponseTestSchema, \
    GetContractDocumentResponseTestSchema
from tests.schema.operations import GetOperationReceiptResponseTestSchema
from tests.tools.logger import get_test_logger

logger = get_test_logger("DOCUMENTS_GATEWAY_ASSERTIONS")

@allure.step("Check tariff document")
def assert_tariff_document(actual: TariffTestSchema, expected: TariffTestSchema) -> None:
    logger.info("Check tariff document")

    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")

@allure.step("Check contract document")
def assert_contract_document(actual: ContractTestSchema, expected: ContractTestSchema) -> None:
    logger.info("Check contract document")

    assert_equal(actual.url, expected.url, "url")
    assert_equal(actual.document, expected.document, "document")

@allure.step("Check receipt document")
def assert_receipt_document(actual: GetOperationReceiptResponseTestSchema, expected: GetOperationReceiptResponseTestSchema) -> None:
    logger.info("Check receipt document")

    assert_equal(actual.receipt.url, expected.receipt.url, "url")
    assert_equal(actual.receipt.document, expected.receipt.document, "document")

@allure.step("Check get tariff document response")
def assert_get_tariff_document_response(actual: GetTariffDocumentResponseTestSchema, expected: GetTariffDocumentResponseTestSchema) -> None:
    logger.info("Check get tariff document response")

    assert_tariff_document(actual.tariff, expected.tariff)

@allure.step("Check get contract document response")
def assert_get_contract_document_response(actual: GetContractDocumentResponseTestSchema, expected: GetContractDocumentResponseTestSchema) -> None:
    logger.info("Check get tariff document response")

    assert_contract_document(actual.contract, expected.contract)

@allure.step("Check get receipt document response")
def assert_get_operation_receipt_response(actual: GetOperationReceiptResponseTestSchema, expected: GetOperationReceiptResponseTestSchema) -> None:
    logger.info("Check get receipt document response")

    assert_receipt_document(actual, expected)

@allure.step("Check get tariff document response. User with active debit card account")
def assert_get_tariff_document_response_user_with_active_debit_card_account(actual: GetTariffDocumentResponseTestSchema) -> None:
    logger.info("Check get tariff document response. User with active debit card account")
    expected = GetTariffDocumentResponseTestSchema(tariff=TariffTestSchema(
        url="http://localhost:3000/tariff/document.pdf",
        document="dGFyaWZmLWRvY3VtZW50"
    ))
    
    assert_get_tariff_document_response(actual, expected)


@allure.step("Check get contract document response. User with active debit card account")
def assert_get_contract_document_response_user_with_active_debit_card_account(actual: GetContractDocumentResponseTestSchema) -> None:
    logger.info("Check get contract document response. User with active debit card account")
    expected = GetContractDocumentResponseTestSchema(contract=
        Contract(
            url="http://localhost:3000/contract/document.pdf",
            document="Y29udHJhY3QtZG9jdW1lbnQ="
        )
    )

    assert_get_contract_document_response(actual, expected)


@allure.step("Check get tariff document response. User with one purchase and one top up operations")
def assert_get_tariff_document_response_user_with_one_purchase_and_one_top_up_operations(actual: GetTariffDocumentResponseTestSchema) -> None:
    logger.info("Check get tariff document response. User with one purchase and one top up operations")
    expected = GetTariffDocumentResponseTestSchema(tariff=
        Tariff(
            url="http://localhost:3000/tariff/document.pdf",
            document="dGFyaWZmLWRvY3VtZW50"
        )
    )

    assert_get_tariff_document_response(actual, expected)

@allure.step("Check get contract document response. User with one purchase and one top up operations")
def assert_get_contract_document_response_user_with_one_purchase_and_one_top_up_operations(actual: GetContractDocumentResponseTestSchema) -> None:
    logger.info("Check get contract document response. User with one purchase and one top up operations")
    expected = GetContractDocumentResponseTestSchema(contract=
        Contract(
            url="http://localhost:3000/contract/document.pdf",
            document="Y29udHJhY3QtZG9jdW1lbnQ="
        )
    )

    assert_get_contract_document_response(actual, expected)
    
@allure.step("Check get operation receipt document response. User with one purchase and one top up operations")
def assert_get_operation_receipt_document_response_user_with_one_purchase_and_one_top_up_operations(actual: GetOperationReceiptResponseTestSchema) -> None:
    logger.info("Check get operation receipt document response. User with one purchase and one top up operations")
    expected = GetOperationReceiptResponseTestSchema(receipt=
        Receipt(
            url="http://localhost:3000/receipt/document.pdf",
            document="cmVjZWlwdC1kb2N1bWVudA"
        )
    )

    assert_get_operation_receipt_response(actual, expected)

