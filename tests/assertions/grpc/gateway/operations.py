import allure

from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import GetOperationsSummaryResponse
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
from contracts.services.operations.operation_pb2 import Operation, OperationType, OperationStatus
from contracts.services.operations.operations_summary_pb2 import OperationsSummary
from tests.assertions.base import assert_equal, assert_length
from tests.tools.date import to_proto_test_datetime
from tests.tools.logger import get_test_logger

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

@allure.step("Check get operations summary")
def assert_get_operations_summary(actual: OperationsSummary, expected: OperationsSummary) -> None:
    logger.info("Check get operations summary")

    assert_equal(actual.cashback_amount, expected.cashback_amount, "Cashback amount")
    assert_equal(actual.received_amount, expected.received_amount, "Received amount")
    assert_equal(actual.spent_amount, expected.spent_amount, "Spent amount")

@allure.step("Check get operations response")
def assert_get_operations_response(
       actual: GetOperationsResponse,
       expected: GetOperationsResponse
) -> None:
    logger.info("Check get operations response")

    assert_length(actual.operations, expected.operations, "Operations list")
    for index, operation in enumerate(expected.operations):
        assert_operation(actual.operations[index], operation)

@allure.step("Check get operations summary response")
def assert_get_operations_summary_response(
        actual: GetOperationsSummaryResponse,
        expected: GetOperationsSummaryResponse
) -> None:
    logger.info("Check get operations summary response")

    assert_get_operations_summary(actual.summary, expected.summary)

@allure.step("Check get operation response")
def assert_get_operation_response(
    actual: GetOperationResponse,
    expected: GetOperationResponse
) -> None:
    logger.info("Check get operation response")

    assert_operation(actual.operation, expected.operation)

@allure.step("Check make fee operation response")
def assert_make_fee_operation_response(
        actual: MakeFeeOperationResponse,
        expected: MakeFeeOperationResponse
) -> None:
    logger.info("Check make fee operation response")

    assert_operation(actual.operation, expected.operation)

@allure.step("Check make cash withdrawal operation response")
def assert_make_cash_withdrawal_operation_response(
        actual: MakeCashWithdrawalOperationResponse,
        expected: MakeCashWithdrawalOperationResponse
) -> None:
    logger.info("Check make cash withdrawal operation response")

    assert_operation(actual.operation, expected.operation)

@allure.step("Check make bill payment operation response")
def assert_make_bill_payment_operation_response(
        actual: MakeBillPaymentOperationResponse,
        expected: MakeBillPaymentOperationResponse
) -> None:
    logger.info("Check make bill payment operation response")

    assert_operation(actual.operation, expected.operation)

@allure.step("Check make top up operation response")
def assert_make_top_up_operation_response(
        actual: MakeTopUpOperationResponse,
        expected: MakeTopUpOperationResponse
) -> None:
    logger.info("Check make top up operation response")

    assert_operation(actual.operation, expected.operation)

@allure.step("Check make cashback operation response")
def assert_make_cashback_operation_response(
        actual: MakeCashbackOperationResponse,
        expected: MakeCashbackOperationResponse
) -> None:
    logger.info("Check make cashback operation response")

    assert_operation(actual.operation, expected.operation)

@allure.step("Check make transfer operation response")
def assert_make_transfer_operation_response(
        actual: MakeTransferOperationResponse,
        expected: MakeTransferOperationResponse
) -> None:
    logger.info("Check make transfer operation response")

    assert_operation(actual.operation, expected.operation)

@allure.step("Check make purchase operation response")
def assert_make_purchase_operation_response(
        actual: MakePurchaseOperationResponse,
        expected: MakePurchaseOperationResponse
) -> None:
    logger.info("Check make purchase operation response")

    assert_operation(actual.operation, expected.operation)


@allure.step("Check get operations response. User with active debit card account")
def assert_get_operations_response_user_with_active_debit_card_account(actual: GetOperationsResponse) -> None:
    logger.info("Check get operations response. User with active debit card account")

    expected = GetOperationsResponse(operations=[])

    assert_get_operations_response(actual, expected)

@allure.step("Check get operations summary response. User with active debit card account")
def assert_get_operations_summary_response_user_with_active_debit_card_account(actual: GetOperationsSummaryResponse) -> None:
    logger.info("Check get operations summary response. User with active debit card account")

    expected = GetOperationsSummaryResponse(summary= OperationsSummary(
        spentAmount=0,
        receivedAmount=0,
        cashbackAmount=0,
        )
    )
    assert_get_operations_summary_response(actual, expected)

@allure.step("Check make purchase operation response. User with active debit card account")
def assert_make_purchase_operation_response_user_with_active_debit_card_account(actual: MakePurchaseOperationResponse) -> None:
    logger.info("Check make purchase operation response. User with active debit card account")

    expected = MakePurchaseOperationResponse(operation=Operation(
                id= "b08b7e07-0919-44f4-a3a9-81c048def897",
                type=OperationType.OPERATION_TYPE_PURCHASE,
                status=OperationStatus.OPERATION_STATUS_COMPLETED,
                amount= -77.99,
                cardId= "96af71f1-5739-4147-bb55-19474c9afa78",
                category= "taxi",
                createdAt= "2025-06-27T16:50:06.374Z",
                accountId= "25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8"
    ))
    assert_make_purchase_operation_response(actual, expected)


@allure.step("Check get operations response. User with one purchase and one top up operations")
def assert_get_operations_response_user_with_one_purchase_and_one_top_up_operations(actual: GetOperationsResponse) -> None:
    logger.info("Check get operations response. User with one purchase and one top up operations")

    expected = GetOperationsResponse(operations=[
        Operation(
            id="2b75538b-c63d-4451-8806-7cca8ad5ae81",
            type=OperationType.OPERATION_TYPE_PURCHASE,
            status=OperationStatus.OPERATION_STATUS_COMPLETED,
            amount=-2500,
            cardId="09c4b3c3-1a9b-474d-925f-d543c027ece5",
            category="taxi",
            createdAt="2025-06-27T16:50:06.374Z",
            accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8"
        ),
        Operation(
            id="1cbce86b-484b-46cd-9ae7-3cff96b0700f",
            type=OperationType.OPERATION_TYPE_TOP_UP,
            status=OperationStatus.OPERATION_STATUS_IN_PROGRESS,
            amount=15000,
            cardId="09c4b3c3-1a9b-474d-925f-d543c027ece5",
            category="money_in",
            createdAt="2025-06-27T16:50:06.374Z",
            accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8"
        )
    ])

    assert_get_operations_response(actual, expected)

@allure.step("Check get operation response. User with one purchase and one top up operations")
def assert_get_operation_response_user_with_one_purchase_and_one_top_up_operations(actual: GetOperationResponse) -> None:
    logger.info("Check get operation response. User with one purchase and one top up operations")

    expected = GetOperationResponse(operation=Operation(
        id="2b75538b-c63d-4451-8806-7cca8ad5ae81",
        type=OperationType.OPERATION_TYPE_PURCHASE,
        status=OperationStatus.OPERATION_STATUS_COMPLETED,
        amount=-2500,
        cardId="09c4b3c3-1a9b-474d-925f-d543c027ece5",
        category="taxi",
        createdAt="2025-06-27T16:50:06.374Z",
        accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8"
    ))

    assert_get_operation_response(actual, expected)


@allure.step("Check get operations summary response. User with one purchase and one top up operations")
def assert_get_operations_summary_response_user_with_one_purchase_and_one_top_up_operations(
        actual: GetOperationsSummaryResponse
        ) -> None:
    logger.info("Check get operations summary response. User with one purchase and one top up operations")

    expected = GetOperationsSummaryResponse(
        summary=OperationsSummary(
            spentAmount=2500,
            receivedAmount=15000,
            cashbackAmount=0,
        )
    )
    assert_get_operations_summary_response(actual, expected)


@allure.step("Check make purchase operation response. User with one purchase and one top up operations")
def assert_make_purchase_operation_response_user_with_user_with_one_purchase_and_one_top_up_operations(
        actual: MakePurchaseOperationResponse
        ) -> None:
    logger.info("Check make purchase operation response. User with one purchase and one top up operations")

    expected = MakePurchaseOperationResponse(
        operation=Operation(
            id="b08b7e07-0919-44f4-a3a9-81c048def897",
            type=OperationType.OPERATION_TYPE_PURCHASE,
            status=OperationStatus.OPERATION_STATUS_COMPLETED,
            amount=-77.99,
            cardId="ac532047-f67a-4dad-9fe5-3f71a1553cb8",
            category="taxi",
            createdAt="2025-06-27T16:50:06.374Z",
            accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8"
        )
    )
    assert_make_purchase_operation_response(actual, expected)