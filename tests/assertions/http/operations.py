import allure

from tests.assertions.base import assert_equal, assert_length
from tests.schema.operations import (
    OperationTestSchema,
    GetOperationsResponseTestSchema,
    GetOperationResponseTestSchema,
    MakeFeeOperationRequestTestSchema,
    MakeFeeOperationResponseTestSchema,
    MakeTopUpOperationResponseTestSchema,
    MakeTopUpOperationRequestTestSchema,
    MakeCashbackOperationRequestTestSchema,
    MakeCashbackOperationResponseTestSchema,
    MakeTransferOperationRequestTestSchema,
    MakeTransferOperationResponseTestSchema,
    MakePurchaseOperationRequestTestSchema,
    MakePurchaseOperationResponseTestSchema,
    MakeBillPaymentOperationRequestTestSchema,
    MakeBillPaymentOperationResponseTestSchema,
    MakeCashWithdrawalOperationRequestTestSchema,
    MakeCashWithdrawalOperationResponseTestSchema
)
from tests.tools.logger import get_test_logger
from tests.types.operations import OperationTestType

logger = get_test_logger("OPERATIONS_GATEWAY_ASSERTIONS")

@allure.step("Check operation")
def assert_operation(actual: OperationTestSchema, expected: OperationTestSchema) -> None:
    logger.info("Check operation")

    assert_equal(actual.status, expected.status, "status")
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.account_id, expected.account_id, "account_id")
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.card_id, expected.card_id, "card_id")
    assert_equal(actual.amount, expected.amount, "amount")
    assert_equal(actual.category, expected.category, "category")
    assert_equal(actual.created_at, expected.created_at, "created_at")

@allure.step("Check get operations response")
def assert_get_operations_response(
        get_operations_response: GetOperationsResponseTestSchema,
        make_operations_responses: list[OperationTestSchema]
) -> None:
    logger.info("Check get operations response")

    assert_length(get_operations_response.operations, make_operations_responses, "Operations list")
    for index, operation in enumerate(make_operations_responses):
        assert_operation(get_operations_response.operations[index], operation)

@allure.step("Check get operation response")
def assert_get_operation_response(
    get_operation_response: GetOperationResponseTestSchema,
    make_operation_response: OperationTestSchema
) -> None:
    logger.info("Check get operation response")

    assert_operation(get_operation_response.operation, make_operation_response)

@allure.step("Check make fee operation response")
def assert_make_fee_operation_response(
        request: MakeFeeOperationRequestTestSchema,
        response: MakeFeeOperationResponseTestSchema
) -> None:
    logger.info("Check make fee operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, -request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationTestType.FEE, "type")

@allure.step("Check make cash withdrawal operation response")
def assert_make_cash_withdrawal_operation_response(
        request: MakeCashWithdrawalOperationRequestTestSchema,
        response: MakeCashWithdrawalOperationResponseTestSchema
) -> None:
    logger.info("Check make cash withdrawal operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, -request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationTestType.CASH_WITHDRAWAL, "type")

@allure.step("Check make bill payment operation response")
def assert_make_bill_payment_operation_response(
        request: MakeBillPaymentOperationRequestTestSchema,
        response: MakeBillPaymentOperationResponseTestSchema
) -> None:
    logger.info("Check make bill payment operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, -request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationTestType.BILL_PAYMENT, "type")

@allure.step("Check make top up operation response")
def assert_make_top_up_operation_response(
        request: MakeTopUpOperationRequestTestSchema,
        response: MakeTopUpOperationResponseTestSchema
) -> None:
    logger.info("Check make top up operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationTestType.TOP_UP, "type")

@allure.step("Check make cashback operation response")
def assert_make_cashback_operation_response(
        request: MakeCashbackOperationRequestTestSchema,
        response: MakeCashbackOperationResponseTestSchema
) -> None:
    logger.info("Check make cashback operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationTestType.CASHBACK, "type")

@allure.step("Check make transfer operation response")
def assert_make_transfer_operation_response(
        request: MakeTransferOperationRequestTestSchema,
        response: MakeTransferOperationResponseTestSchema
) -> None:
    logger.info("Check make transfer operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, -request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationTestType.TRANSFER, "type")

@allure.step("Check make purchase operation response")
def assert_make_purchase_operation_response(
        request: MakePurchaseOperationRequestTestSchema,
        response: MakePurchaseOperationResponseTestSchema
) -> None:
    logger.info("Check make purchase operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, -request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationTestType.PURCHASE, "type")
    assert_equal(response.operation.category, request.category, "category")