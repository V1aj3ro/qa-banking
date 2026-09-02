import allure
from grpc import Channel

from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse
)
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse
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
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse
)
from contracts.services.operations.operation_pb2 import OperationStatus
from tests.clients.grpc.client import GRPCTestClient
from tests.clients.grpc.gateway.client import build_gateway_grpc_test_client
from tests.tools.fakers import fake

from tests.tools.logger import get_test_logger


class OperationsGatewayGRPCTestClient(GRPCTestClient):

    def __init__(self, channel: Channel):
        super().__init__(channel)

        self.stub = OperationsGatewayServiceStub(channel)

    @allure.step("Get operation")
    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        return self.stub.GetOperation(request)

    @allure.step("Get operation receipt")
    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        return self.stub.GetOperationReceipt(request)

    @allure.step("Get operations")
    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        return self.stub.GetOperations(request)

    @allure.step("Get operations summary")
    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        return self.stub.GetOperationsSummary(request)

    @allure.step("Make fee operation")
    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        return self.stub.MakeFeeOperation(request)

    @allure.step("Make top up operation")
    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        return self.stub.MakeTopUpOperation(request)

    @allure.step("Make cashback operation")
    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        return self.stub.MakeCashbackOperation(request)

    @allure.step("Make transfer operation")
    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        return self.stub.MakeTransferOperation(request)

    @allure.step("Make purchase operation")
    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        return self.stub.MakePurchaseOperation(request)

    @allure.step("Make bill payment operation")
    def make_bill_payment_operation_api(
            self,
            request: MakeBillPaymentOperationRequest
    ) -> MakeBillPaymentOperationResponse:
        return self.stub.MakeBillPaymentOperation(request)

    @allure.step("Make cash withdrawal operation")
    def make_cash_withdrawal_operation_api(
            self,
            request: MakeCashWithdrawalOperationRequest
    ) -> MakeCashWithdrawalOperationResponse:
        return self.stub.MakeCashWithdrawalOperation(request)

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        request = MakeFeeOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        request = MakeTopUpOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponse:
        request = MakeCashbackOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponse:
        request = MakeTransferOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponse:
        request = MakePurchaseOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            category=fake.category(),
            account_id=account_id
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponse:
        request = MakeBillPaymentOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponse:
        request = MakeCashWithdrawalOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cash_withdrawal_operation_api(request)


def build_operations_gateway_grpc_test_client() -> OperationsGatewayGRPCTestClient:
    return OperationsGatewayGRPCTestClient(channel=build_gateway_grpc_test_client(
        logger=get_test_logger("OPERATIONS_GATEWAY_GRPC_TEST_CLIENT")
        )
    )

