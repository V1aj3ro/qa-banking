import allure

from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsResponse
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationResponse,
    MakeCashWithdrawalOperationRequest
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse
)
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationResponse,
    MakePurchaseOperationRequest
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse
)
from contracts.services.operations.operation_pb2 import Operation, OperationType
from tests.assertions.base import assert_equal, assert_length
from tests.tools.logger import get_test_logger
from tests.types.operations import OperationTestType

logger = get_test_logger("OPERATIONS_GATEWAY_ASSERTIONS")

@allure.step("Check operation")
def assert_operation(actual: Operation, expected: Operation) -> None:
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
        get_operations_response: GetOperationsResponse,
        make_operations_responses: list[Operation]
) -> None:
    logger.info("Check get operations response")

    assert_length(get_operations_response.operations, make_operations_responses, "Operations list")
    for index, operation in enumerate(make_operations_responses):
        assert_operation(get_operations_response.operations[index], operation)

@allure.step("Check get operation response")
def assert_get_operation_response(
    get_operation_response: GetOperationResponse,
    make_operation_response: Operation
) -> None:
    logger.info("Check get operation response")

    assert_operation(get_operation_response.operation, make_operation_response)

@allure.step("Check make fee operation response")
def assert_make_fee_operation_response(
        request: MakeFeeOperationRequest,
        response: MakeFeeOperationResponse
) -> None:
    logger.info("Check make fee operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, -request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationType.OPERATION_TYPE_FEE, "type")

@allure.step("Check make cash withdrawal operation response")
def assert_make_cash_withdrawal_operation_response(
        request: MakeCashWithdrawalOperationRequest,
        response: MakeCashWithdrawalOperationResponse
) -> None:
    logger.info("Check make cash withdrawal operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, -request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationType.OPERATION_TYPE_CASH_WITHDRAWAL, "type")

@allure.step("Check make bill payment operation response")
def assert_make_bill_payment_operation_response(
        request: MakeBillPaymentOperationRequest,
        response: MakeBillPaymentOperationResponse
) -> None:
    logger.info("Check make bill payment operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, -request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationType.OPERATION_TYPE_BILL_PAYMENT, "type")

@allure.step("Check make top up operation response")
def assert_make_top_up_operation_response(
        request: MakeTopUpOperationRequest,
        response: MakeTopUpOperationResponse
) -> None:
    logger.info("Check make top up operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationType.OPERATION_TYPE_TOP_UP, "type")

@allure.step("Check make cashback operation response")
def assert_make_cashback_operation_response(
        request: MakeCashbackOperationRequest,
        response: MakeCashbackOperationResponse
) -> None:
    logger.info("Check make cashback operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationType.OPERATION_TYPE_CASHBACK, "type")

@allure.step("Check make transfer operation response")
def assert_make_transfer_operation_response(
        request: MakeTransferOperationRequest,
        response: MakeTransferOperationResponse
) -> None:
    logger.info("Check make transfer operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, -request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationType.OPERATION_TYPE_TRANSFER, "type")

@allure.step("Check make purchase operation response")
def assert_make_purchase_operation_response(
        request: MakePurchaseOperationRequest,
        response: MakePurchaseOperationResponse
) -> None:
    logger.info("Check make purchase operation response")

    assert_equal(response.operation.status, request.status, "status")
    assert_equal(response.operation.amount, -request.amount, "amount")
    assert_equal(response.operation.card_id, request.card_id, "card_id")
    assert_equal(response.operation.account_id, request.account_id, "account_id")
    assert_equal(response.operation.type, OperationType.OPERATION_TYPE_PURCHASE, "type")
    assert_equal(response.operation.category, request.category, "category")