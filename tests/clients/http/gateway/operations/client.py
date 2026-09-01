import allure
from httpx import Response, QueryParams

from tests.clients.http.client import HTTPTestClient
from tests.schema.operations import (
    GetOperationReceiptResponseTestSchema,
    GetOperationResponseTestSchema,
    GetOperationsQueryTestSchema,
    GetOperationsResponseTestSchema,
    GetOperationsSummaryQueryTestSchema,
    GetOperationsSummaryResponseTestSchema,
    MakeBillPaymentOperationRequestTestSchema,
    MakeBillPaymentOperationResponseTestSchema,
    MakeCashbackOperationRequestTestSchema,
    MakeCashbackOperationResponseTestSchema,
    MakeCashWithdrawalOperationRequestTestSchema,
    MakeCashWithdrawalOperationResponseTestSchema,
    MakeFeeOperationRequestTestSchema,
    MakeFeeOperationResponseTestSchema,
    MakePurchaseOperationRequestTestSchema,
    MakePurchaseOperationResponseTestSchema,
    MakeTopUpOperationRequestTestSchema,
    MakeTopUpOperationResponseTestSchema,
    MakeTransferOperationRequestTestSchema,
    MakeTransferOperationResponseTestSchema
)
from tests.tools.routes import APITestRoutes

from tests.clients.http.gateway.client import build_gateway_http_test_client
from tests.tools.logger import get_test_logger


class OperationsGatewayHTTPTestClient(HTTPTestClient):

    @allure.step("Get operation")
    def get_operation_api(self, operation_id: str) -> Response:
        return self.get(
            f"{APITestRoutes.OPERATIONS}/{operation_id}",
        )

    @allure.step("Get operation receipt")
    def get_operation_receipt_api(self, operation_id: str) -> Response:
        return self.get(
            f"{APITestRoutes.OPERATIONS}/operation-receipt/{operation_id}",
        )

    @allure.step("Get operations")
    def get_operations_api(self, query: GetOperationsQueryTestSchema) -> Response:
        return self.get(
            APITestRoutes.OPERATIONS,
            params=QueryParams(**query.model_dump(by_alias=True)),
        )

    @allure.step("Get operations summary")
    def get_operations_summary_api(self, query: GetOperationsSummaryQueryTestSchema) -> Response:
        return self.get(
            f"{APITestRoutes.OPERATIONS}/operations-summary",
            params=QueryParams(**query.model_dump(by_alias=True)),
        )

    @allure.step("Make fee operation")
    def make_fee_operation_api(self, request: MakeFeeOperationRequestTestSchema) -> Response:
        return self.post(f"{APITestRoutes.OPERATIONS}/make-fee-operation", json=request.model_dump(by_alias=True))

    @allure.step("Make top up operation")
    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestTestSchema) -> Response:
        return self.post(f"{APITestRoutes.OPERATIONS}/make-top-up-operation", json=request.model_dump(by_alias=True))

    @allure.step("Make cashback operation")
    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestTestSchema) -> Response:
        return self.post(f"{APITestRoutes.OPERATIONS}/make-cashback-operation", json=request.model_dump(by_alias=True))

    @allure.step("Make transfer operation")
    def make_transfer_operation_api(self, request: MakeTransferOperationRequestTestSchema) -> Response:
        return self.post(f"{APITestRoutes.OPERATIONS}/make-transfer-operation", json=request.model_dump(by_alias=True))

    @allure.step("Make purchase operation")
    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestTestSchema) -> Response:
        return self.post(f"{APITestRoutes.OPERATIONS}/make-purchase-operation", json=request.model_dump(by_alias=True))

    @allure.step("Make bill payment operation")
    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestTestSchema) -> Response:
        return self.post(f"{APITestRoutes.OPERATIONS}/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    @allure.step("Make cash withdrawal operation")
    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestTestSchema) -> Response:
        return self.post(f"{APITestRoutes.OPERATIONS}/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> GetOperationResponseTestSchema:
        response = self.get_operation_api(operation_id)
        return GetOperationResponseTestSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseTestSchema:
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseTestSchema.model_validate_json(response.text)

    def get_operations(self, query: GetOperationsQueryTestSchema) -> GetOperationsResponseTestSchema:
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, query: GetOperationsSummaryQueryTestSchema) -> GetOperationsSummaryResponseTestSchema:
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseTestSchema.model_validate_json(response.text)

    def make_fee_operation(self, request: MakeFeeOperationRequestTestSchema) -> MakeFeeOperationResponseTestSchema:
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseTestSchema.model_validate_json(response.text)

    def make_top_up_operation(self, request: MakeTopUpOperationRequestTestSchema) -> MakeTopUpOperationResponseTestSchema:
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseTestSchema.model_validate_json(response.text)

    def make_cashback_operation(self, request: MakeCashbackOperationRequestTestSchema) -> MakeCashbackOperationResponseTestSchema:
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseTestSchema.model_validate_json(response.text)

    def make_transfer_operation(self, request: MakeTransferOperationRequestTestSchema) -> MakeTransferOperationResponseTestSchema:
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseTestSchema.model_validate_json(response.text)

    def make_purchase_operation(self, request: MakePurchaseOperationRequestTestSchema) -> MakePurchaseOperationResponseTestSchema:
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseTestSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, request: MakeBillPaymentOperationRequestTestSchema) -> MakeBillPaymentOperationResponseTestSchema:
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseTestSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, request: MakeCashWithdrawalOperationRequestTestSchema) -> MakeCashWithdrawalOperationResponseTestSchema:
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseTestSchema.model_validate_json(response.text)


def build_operations_gateway_http_test_client() -> OperationsGatewayHTTPTestClient:
    return OperationsGatewayHTTPTestClient(client=build_gateway_http_test_client(
        logger=get_test_logger("USERS_GATEWAY_HTTP_TEST_CLIENT")
        )
    )

