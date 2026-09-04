from time import sleep

import allure
import pytest

from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import GetOperationReceiptRequest
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import GetOperationsSummaryRequest
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import MakeBillPaymentOperationRequest
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import MakeCashbackOperationRequest
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import MakeFeeOperationRequest
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import MakePurchaseOperationRequest
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import MakeTopUpOperationRequest
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import MakeTransferOperationRequest
from tests.assertions.grpc.operations import (
    assert_make_fee_operation_response,
    assert_make_top_up_operation_response,
    assert_make_cashback_operation_response,
    assert_make_transfer_operation_response,
    assert_make_purchase_operation_response,
    assert_make_bill_payment_operation_response,
    assert_make_cash_withdrawal_operation_response,
    assert_get_operations_response,
    assert_get_operation_response
)
from tests.clients.grpc.gateway.operations.client import OperationsGatewayGRPCTestClient
from tests.fixtures.grpc.gateway.accounts.schema import (
    DepositAccountGRPCFixture,
    CreditCardAccountGRPCFixture,
)
from tests.fixtures.grpc.gateway.accounts.fixtures import function_credit_card_grpc_account
from tests.fixtures.grpc.gateway.cards.schema import VirtualCardGRPCFixture
from tests.fixtures.grpc.gateway.operations.schema import FeeOperationGRPCFixture
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_operations
@pytest.mark.regression
@pytest.mark.positive
@allure.tag(AllureTag.GRPC, AllureTag.GATEWAY_SERVICE, AllureTag.POSITIVE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.OPERATIONS_GATEWAY_SERVICE)
class TestOperationsGRPC:
    @allure.story(AllureStory.GET_OPERATIONS)
    @allure.title("[gRPC] Get operations")
    def test_get_operations(
            self,
            function_credit_card_grpc_account: CreditCardAccountGRPCFixture,
            function_fee_grpc_operation: FeeOperationGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        query = GetOperationsRequest(account_id=function_credit_card_grpc_account.id)
        response = operations_gateway_grpc_test_client.get_operations_api(query)

        assert_get_operations_response(response, [function_fee_grpc_operation.response.operation])


    @allure.story(AllureStory.GET_OPERATIONS_SUMMARY)
    @allure.title("[gRPC] Get operations summary")
    def test_get_operations_summary(
            self,
            function_credit_card_grpc_account: CreditCardAccountGRPCFixture,
            function_fee_grpc_operation: FeeOperationGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        request = GetOperationsSummaryRequest(account_id=function_credit_card_grpc_account.id)
        response = operations_gateway_grpc_test_client.get_operations_summary_api(request)


    @allure.story(AllureStory.GET_OPERATION_RECEIPT)
    @allure.title("[gRPC] Get operation receipt")
    def test_get_operations_receipt(
            self,
            function_credit_card_grpc_account: CreditCardAccountGRPCFixture,
            function_fee_grpc_operation: FeeOperationGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        request = GetOperationReceiptRequest(operation_id = function_fee_grpc_operation.id)
        response = operations_gateway_grpc_test_client.get_operation_receipt_api(request)


    @allure.story(AllureStory.GET_OPERATION)
    @allure.title("[gRPC] Get operation")
    def test_get_operation(
            self,
            function_credit_card_grpc_account: CreditCardAccountGRPCFixture,
            function_fee_grpc_operation: FeeOperationGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        request = GetOperationRequest(id = function_fee_grpc_operation.id)
        response = operations_gateway_grpc_test_client.get_operation_api(request)

        assert_get_operation_response(response, function_fee_grpc_operation.response.operation)



    @allure.story(AllureStory.MAKE_FEE_OPERATION)
    @allure.title("[gRPC] Make fee operation")
    def test_make_fee_operation(
            self,
            function_virtual_grpc_card: VirtualCardGRPCFixture,
            function_deposit_grpc_account: DepositAccountGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        request = MakeFeeOperationRequest(
            account_id=function_deposit_grpc_account.id,
            card_id=function_virtual_grpc_card.id
        )
        response = operations_gateway_grpc_test_client.make_fee_operation_api(request)


        assert_make_fee_operation_response(request, response)

    @allure.story(AllureStory.MAKE_TOP_UP_OPERATION)
    @allure.title("[gRPC] Make top up operation")
    def test_make_top_up_operation(
            self,
            function_virtual_grpc_card: VirtualCardGRPCFixture,
            function_deposit_grpc_account: DepositAccountGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        request = MakeTopUpOperationRequest(
            account_id=function_deposit_grpc_account.id,
            card_id=function_virtual_grpc_card.id
        )
        response = operations_gateway_grpc_test_client.make_top_up_operation_api(request)

        assert_make_top_up_operation_response(request, response)

    @allure.story(AllureStory.MAKE_CASHBACK_OPERATION)
    @allure.title("[gRPC] Make cashback operation")
    def test_make_cashback_operation(
            self,
            function_virtual_grpc_card: VirtualCardGRPCFixture,
            function_deposit_grpc_account: DepositAccountGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        request = MakeCashbackOperationRequest(
            account_id=function_deposit_grpc_account.id,
            card_id=function_virtual_grpc_card.id
        )
        response = operations_gateway_grpc_test_client.make_cashback_operation_api(request)

        assert_make_cashback_operation_response(request, response)

    @allure.story(AllureStory.MAKE_TRANSFER_OPERATION)
    @allure.title("[gRPC] Make transfer operation")
    def test_make_transfer_operation(
            self,
            function_virtual_grpc_card: VirtualCardGRPCFixture,
            function_deposit_grpc_account: DepositAccountGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        request = MakeTransferOperationRequest(
            account_id=function_deposit_grpc_account.id,
            card_id=function_virtual_grpc_card.id
        )
        response = operations_gateway_grpc_test_client.make_transfer_operation_api(request)

        assert_make_transfer_operation_response(request, response)

    @allure.story(AllureStory.MAKE_PURCHASE_OPERATION)
    @allure.title("[gRPC] Make purchase operation")
    def test_make_purchase_operation(
            self,
            function_virtual_grpc_card: VirtualCardGRPCFixture,
            function_deposit_grpc_account: DepositAccountGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        request = MakePurchaseOperationRequest(
            account_id=function_deposit_grpc_account.id,
            card_id=function_virtual_grpc_card.id
        )
        response = operations_gateway_grpc_test_client.make_purchase_operation_api(request)

        assert_make_purchase_operation_response(request, response)

    @allure.story(AllureStory.MAKE_BILL_PAYMENT_OPERATION)
    @allure.title("[gRPC] Make bill payment operation")
    def test_make_bill_payment_operation(
            self,
            function_virtual_grpc_card: VirtualCardGRPCFixture,
            function_deposit_grpc_account: DepositAccountGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        request = MakeBillPaymentOperationRequest(
            account_id=function_deposit_grpc_account.id,
            card_id=function_virtual_grpc_card.id
        )
        response = operations_gateway_grpc_test_client.make_bill_payment_operation_api(request)


        assert_make_bill_payment_operation_response(request, response)


    @allure.story(AllureStory.MAKE_CASH_WITHDRAWAL_OPERATION)
    @allure.title("[gRPC] Make cash withdrawal operation")
    def test_make_cash_withdrawal_operation(
            self,
            function_virtual_grpc_card: VirtualCardGRPCFixture,
            function_deposit_grpc_account: DepositAccountGRPCFixture,
            operations_gateway_grpc_test_client: OperationsGatewayGRPCTestClient
    ):
        request = MakeCashWithdrawalOperationRequest(
            account_id=function_deposit_grpc_account.id,
            card_id=function_virtual_grpc_card.id
        )
        response = operations_gateway_grpc_test_client.make_cash_withdrawal_operation_api(request)

        assert_make_cash_withdrawal_operation_response(request, response)

