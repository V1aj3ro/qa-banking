from typing import Optional

from tests.context.base import build_grpc_test_metadata, RequestContext
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
    def get_operation_api(
            self,
            request: GetOperationRequest,
            context: Optional[RequestContext] = None
    ) -> GetOperationResponse:
        return self.stub.GetOperation(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Get operation receipt")
    def get_operation_receipt_api(
            self,
            request: GetOperationReceiptRequest,
            context: Optional[RequestContext] = None
    ) -> GetOperationReceiptResponse:
        return self.stub.GetOperationReceipt(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Get operations")
    def get_operations_api(
            self,
            request: GetOperationsRequest,
            context: Optional[RequestContext] = None
    ) -> GetOperationsResponse:
        return self.stub.GetOperations(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Get operations summary")
    def get_operations_summary_api(
            self,
            request: GetOperationsSummaryRequest,
            context: Optional[RequestContext] = None
    ) -> GetOperationsSummaryResponse:
        return self.stub.GetOperationsSummary(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Make fee operation")
    def make_fee_operation_api(
            self,
            request: MakeFeeOperationRequest,
            context: Optional[RequestContext] = None
    ) -> MakeFeeOperationResponse:
        return self.stub.MakeFeeOperation(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Make top up operation")
    def make_top_up_operation_api(
            self,
            request: MakeTopUpOperationRequest,
            context: Optional[RequestContext] = None
    ) -> MakeTopUpOperationResponse:
        return self.stub.MakeTopUpOperation(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Make cashback operation")
    def make_cashback_operation_api(
            self,
            request: MakeCashbackOperationRequest,
            context: Optional[RequestContext] = None
    ) -> MakeCashbackOperationResponse:
        return self.stub.MakeCashbackOperation(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Make transfer operation")
    def make_transfer_operation_api(
            self,
            request: MakeTransferOperationRequest,
            context: Optional[RequestContext] = None
    ) -> MakeTransferOperationResponse:
        return self.stub.MakeTransferOperation(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Make purchase operation")
    def make_purchase_operation_api(
            self,
            request: MakePurchaseOperationRequest,
            context: Optional[RequestContext] = None
    ) -> MakePurchaseOperationResponse:
        return self.stub.MakePurchaseOperation(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Make bill payment operation")
    def make_bill_payment_operation_api(
            self,
            request: MakeBillPaymentOperationRequest,
            context: Optional[RequestContext] = None
    ) -> MakeBillPaymentOperationResponse:
        return self.stub.MakeBillPaymentOperation(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    @allure.step("Make cash withdrawal operation")
    def make_cash_withdrawal_operation_api(
            self,
            request: MakeCashWithdrawalOperationRequest,
            context: Optional[RequestContext] = None
    ) -> MakeCashWithdrawalOperationResponse:
        return self.stub.MakeCashWithdrawalOperation(
            request,
            metadata=build_grpc_test_metadata(context)
        )

    def get_operation(
            self,
            operation_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> GetOperationResponse:
        if operation_id is None:
            operation_id = str(fake.uuid())
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request, context)

    def get_operation_receipt(
            self,
            operation_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> GetOperationReceiptResponse:
        if operation_id is None:
            operation_id = str(fake.uuid())
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request, context)

    def get_operations(
            self,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> GetOperationsResponse:
        if account_id is None:
            account_id = str(fake.uuid())
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request, context)

    def get_operations_summary(
            self,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> GetOperationsSummaryResponse:
        if account_id is None:
            account_id = str(fake.uuid())
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request, context)

    def make_fee_operation(
            self,
            card_id: Optional[str] = None,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> MakeFeeOperationResponse:
        if card_id is None:
            card_id = str(fake.uuid())
        if account_id is None:
            account_id = str(fake.uuid())
        request = MakeFeeOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_fee_operation_api(request, context)

    def make_top_up_operation(
            self,
            card_id: Optional[str] = None,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> MakeTopUpOperationResponse:
        if card_id is None:
            card_id = str(fake.uuid())
        if account_id is None:
            account_id = str(fake.uuid())
        request = MakeTopUpOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_top_up_operation_api(request, context)

    def make_cashback_operation(
            self,
            card_id: Optional[str] = None,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> MakeCashbackOperationResponse:
        if card_id is None:
            card_id = str(fake.uuid())
        if account_id is None:
            account_id = str(fake.uuid())
        request = MakeCashbackOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cashback_operation_api(request, context)

    def make_transfer_operation(
            self,
            card_id: Optional[str] = None,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> MakeTransferOperationResponse:
        if card_id is None:
            card_id = str(fake.uuid())
        if account_id is None:
            account_id = str(fake.uuid())
        request = MakeTransferOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_transfer_operation_api(request, context)

    def make_purchase_operation(
            self,
            card_id: Optional[str] = None,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> MakePurchaseOperationResponse:
        if card_id is None:
            card_id = str(fake.uuid())
        if account_id is None:
            account_id = str(fake.uuid())
        request = MakePurchaseOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            category=fake.category(),
            account_id=account_id
        )
        return self.make_purchase_operation_api(request, context)

    def make_bill_payment_operation(
            self,
            card_id: Optional[str] = None,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    )-> MakeBillPaymentOperationResponse:
        if card_id is None:
            card_id = str(fake.uuid())
        if account_id is None:
            account_id = str(fake.uuid())
        request = MakeBillPaymentOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_bill_payment_operation_api(request, context)

    def make_cash_withdrawal_operation(
            self,
            card_id: Optional[str] = None,
            account_id: Optional[str] = None,
            context: Optional[RequestContext] = None
    ) -> MakeCashWithdrawalOperationResponse:
        if card_id is None:
            card_id = str(fake.uuid())
        if account_id is None:
            account_id = str(fake.uuid())
        request = MakeCashWithdrawalOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cash_withdrawal_operation_api(request, context)


def build_operations_gateway_grpc_test_client() -> OperationsGatewayGRPCTestClient:
    return OperationsGatewayGRPCTestClient(channel=build_gateway_grpc_test_client(
        logger=get_test_logger("OPERATIONS_GATEWAY_GRPC_TEST_CLIENT")
        )
    )

