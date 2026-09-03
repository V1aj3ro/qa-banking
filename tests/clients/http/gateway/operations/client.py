from typing import Optional

import allure
from httpx import Response, QueryParams

from tests.clients.http.api_coverage import tracker
from tests.clients.http.client import HTTPTestClient
from tests.context.base import RequestContext
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
from tests.tools.fakers import fake
from tests.tools.routes import APITestRoutes

from tests.clients.http.gateway.client import build_gateway_http_test_client
from tests.tools.logger import get_test_logger


class OperationsGatewayHTTPTestClient(HTTPTestClient):

    @allure.step("Get operation")
    @tracker.track_coverage_httpx(f"{APITestRoutes.OPERATIONS}/{{operation_id}}")
    def get_operation_api(self, operation_id: str, context: Optional[RequestContext] = None) -> Response:
        return self.get(
            f"{APITestRoutes.OPERATIONS}/{operation_id}",
            context=context
        )

    @allure.step("Get operation receipt")
    @tracker.track_coverage_httpx(f"{APITestRoutes.OPERATIONS}/operation-receipt/{{operation_id}}")
    def get_operation_receipt_api(self, operation_id: str, context: Optional[RequestContext] = None) -> Response:
        return self.get(
            f"{APITestRoutes.OPERATIONS}/operation-receipt/{operation_id}",
            context=context
        )

    @allure.step("Get operations")
    @tracker.track_coverage_httpx(APITestRoutes.OPERATIONS)
    def get_operations_api(
            self,
            query: GetOperationsQueryTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.get(
            APITestRoutes.OPERATIONS,
            params=QueryParams(**query.model_dump(by_alias=True)),
            context=context
        )

    @allure.step("Get operations summary")
    @tracker.track_coverage_httpx(f"{APITestRoutes.OPERATIONS}/operations-summary")
    def get_operations_summary_api(
            self,
            query: GetOperationsSummaryQueryTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.get(
            f"{APITestRoutes.OPERATIONS}/operations-summary",
            params=QueryParams(**query.model_dump(by_alias=True)),
            context=context
        )

    @allure.step("Make fee operation")
    @tracker.track_coverage_httpx(f"{APITestRoutes.OPERATIONS}/make-fee-operation")
    def make_fee_operation_api(
            self,
            request: MakeFeeOperationRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.OPERATIONS}/make-fee-operation",
            json=request.model_dump(by_alias=True),
            context=context
        )

    @allure.step("Make top up operation")
    @tracker.track_coverage_httpx(f"{APITestRoutes.OPERATIONS}/make-top-up-operation")
    def make_top_up_operation_api(
            self,
            request: MakeTopUpOperationRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.OPERATIONS}/make-top-up-operation",
            json=request.model_dump(by_alias=True),
            context=context
        )

    @allure.step("Make cashback operation")
    @tracker.track_coverage_httpx(f"{APITestRoutes.OPERATIONS}/make-cashback-operation")
    def make_cashback_operation_api(
            self,
            request: MakeCashbackOperationRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.OPERATIONS}/make-cashback-operation",
            json=request.model_dump(by_alias=True),
            context=context
        )

    @allure.step("Make transfer operation")
    @tracker.track_coverage_httpx(f"{APITestRoutes.OPERATIONS}/make-transfer-operation")
    def make_transfer_operation_api(
            self,
            request: MakeTransferOperationRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.OPERATIONS}/make-transfer-operation",
            json=request.model_dump(by_alias=True),
            context=context
        )

    @allure.step("Make purchase operation")
    @tracker.track_coverage_httpx(f"{APITestRoutes.OPERATIONS}/make-purchase-operation")
    def make_purchase_operation_api(
            self,
            request: MakePurchaseOperationRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.OPERATIONS}/make-purchase-operation",
            json=request.model_dump(by_alias=True),
            context=context
        )

    @allure.step("Make bill payment operation")
    @tracker.track_coverage_httpx(f"{APITestRoutes.OPERATIONS}/make-bill-payment-operation")
    def make_bill_payment_operation_api(
            self,
            request: MakeBillPaymentOperationRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.OPERATIONS}/make-bill-payment-operation",
            json=request.model_dump(by_alias=True),
            context=context
        )

    @allure.step("Make cash withdrawal operation")
    @tracker.track_coverage_httpx(f"{APITestRoutes.OPERATIONS}/make-cash-withdrawal-operation")
    def make_cash_withdrawal_operation_api(
            self,
            request: MakeCashWithdrawalOperationRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.OPERATIONS}/make-cash-withdrawal-operation",
            json=request.model_dump(by_alias=True),
            context=context
        )

    def get_operation(
            self,
            operation_id: Optional[str],
            context: Optional[RequestContext] = None
    ) -> GetOperationResponseTestSchema:
        if operation_id is None:
            operation_id=fake.uuid()
        response = self.get_operation_api(operation_id, context)
        return GetOperationResponseTestSchema.model_validate_json(response.text)

    def get_operation_receipt(
            self,
            operation_id: Optional[str],
            context: Optional[RequestContext] = None
    ) -> GetOperationReceiptResponseTestSchema:
        if operation_id is None:
            operation_id=fake.uuid()
        response = self.get_operation_receipt_api(operation_id, context)
        return GetOperationReceiptResponseTestSchema.model_validate_json(response.text)

    def get_operations(
            self,
            query: Optional[GetOperationsQueryTestSchema],
            context: Optional[RequestContext] = None
    ) -> GetOperationsResponseTestSchema:
        if query is None:
            query = GetOperationsQueryTestSchema(account_id=fake.uuid())
        response = self.get_operations_api(query, context)
        return response.json()

    def get_operations_summary(
            self,
            query: Optional[GetOperationsSummaryQueryTestSchema],
            context: Optional[RequestContext] = None
    ) -> GetOperationsSummaryResponseTestSchema:
        if query is None:
            query=GetOperationsSummaryQueryTestSchema(account_id=fake.uuid())
        response = self.get_operations_summary_api(query, context)
        return GetOperationsSummaryResponseTestSchema.model_validate_json(response.text)

    def make_fee_operation(
            self,
            request: Optional[MakeFeeOperationRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> MakeFeeOperationResponseTestSchema:
        if request is None:
            request=MakeFeeOperationRequestTestSchema(card_id=fake.uuid(), account_id=fake.uuid())
        response = self.make_fee_operation_api(request, context)
        return MakeFeeOperationResponseTestSchema.model_validate_json(response.text)

    def make_top_up_operation(
            self,
            request: Optional[MakeTopUpOperationRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> MakeTopUpOperationResponseTestSchema:
        if request is None:
            request=MakeTopUpOperationRequestTestSchema(card_id=fake.uuid(), account_id=fake.uuid())
        response = self.make_top_up_operation_api(request, context)
        return MakeTopUpOperationResponseTestSchema.model_validate_json(response.text)

    def make_cashback_operation(
            self,
            request: Optional[MakeCashbackOperationRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> MakeCashbackOperationResponseTestSchema:
        if request is None:
            request=MakeCashbackOperationRequestTestSchema(card_id=fake.uuid(), account_id=fake.uuid())
        response = self.make_cashback_operation_api(request, context)
        return MakeCashbackOperationResponseTestSchema.model_validate_json(response.text)

    def make_transfer_operation(
            self,
            request: Optional[MakeTransferOperationRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> MakeTransferOperationResponseTestSchema:
        if request is None:
            request=MakeTransferOperationRequestTestSchema(card_id=fake.uuid(), account_id=fake.uuid())
        response = self.make_transfer_operation_api(request, context)
        return MakeTransferOperationResponseTestSchema.model_validate_json(response.text)

    def make_purchase_operation(
            self,
            request: Optional[MakePurchaseOperationRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> MakePurchaseOperationResponseTestSchema:
        if request is None:
            request=MakePurchaseOperationRequestTestSchema(card_id=fake.uuid(), account_id=fake.uuid())
        response = self.make_purchase_operation_api(request, context)
        return MakePurchaseOperationResponseTestSchema.model_validate_json(response.text)

    def make_bill_payment_operation(
            self,
            request: Optional[MakeBillPaymentOperationRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> MakeBillPaymentOperationResponseTestSchema:
        if request is None:
            request=MakeBillPaymentOperationRequestTestSchema(card_id=fake.uuid(), account_id=fake.uuid())
        response = self.make_bill_payment_operation_api(request, context)
        return MakeBillPaymentOperationResponseTestSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(
            self,
            request: Optional[MakeCashWithdrawalOperationRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> MakeCashWithdrawalOperationResponseTestSchema:
        if request is None:
            request=MakeCashWithdrawalOperationRequestTestSchema(card_id=fake.uuid(), account_id=fake.uuid())
        response = self.make_cash_withdrawal_operation_api(request, context)
        return MakeCashWithdrawalOperationResponseTestSchema.model_validate_json(response.text)


def build_operations_gateway_http_test_client() -> OperationsGatewayHTTPTestClient:
    return OperationsGatewayHTTPTestClient(client=build_gateway_http_test_client(
        logger=get_test_logger("USERS_GATEWAY_HTTP_TEST_CLIENT")
        )
    )

