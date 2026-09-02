from http import HTTPStatus
from time import sleep

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.operations import (
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
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.operations.client import OperationsGatewayHTTPTestClient
from tests.fixtures.gateway.accounts import (
    DepositAccountHTTPFixture,
    CreditCardAccountHTTPFixture,
    function_credit_card_http_account
)
from tests.fixtures.gateway.cards import VirtualCardHTTPFixture
from tests.fixtures.gateway.operations import FeeOperationHTTPFixture
from tests.schema.operations import (
    MakeFeeOperationRequestTestSchema,
    MakeFeeOperationResponseTestSchema,
    MakeTopUpOperationRequestTestSchema,
    MakeTopUpOperationResponseTestSchema,
    MakeCashbackOperationRequestTestSchema,
    MakeCashbackOperationResponseTestSchema,
    MakeTransferOperationRequestTestSchema,
    MakeTransferOperationResponseTestSchema,
    MakePurchaseOperationRequestTestSchema,
    MakePurchaseOperationResponseTestSchema,
    MakeBillPaymentOperationRequestTestSchema,
    MakeBillPaymentOperationResponseTestSchema,
    MakeCashWithdrawalOperationRequestTestSchema,
    MakeCashWithdrawalOperationResponseTestSchema,
    GetOperationsQueryTestSchema,
    GetOperationsResponseTestSchema,
    GetOperationResponseTestSchema,
    GetOperationsSummaryQueryTestSchema,
    GetOperationsSummaryResponseTestSchema,
    GetOperationReceiptResponseTestSchema
)
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_operations
@pytest.mark.regression
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.OPERATIONS_GATEWAY_SERVICE)
class TestOperationsHTTP:
    @allure.story(AllureStory.GET_OPERATIONS)
    @allure.title("[HTTP] Get operations")
    def test_get_operations(
            self,
            function_credit_card_http_account: CreditCardAccountHTTPFixture,
            function_fee_http_operation: FeeOperationHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        query = GetOperationsQueryTestSchema(account_id=function_credit_card_http_account.id)
        response = operations_gateway_http_test_client.get_operations_api(query)
        response_data = GetOperationsResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_operations_response(response_data, [function_fee_http_operation.response.operation])

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_OPERATIONS_SUMMARY)
    @allure.title("[HTTP] Get operations summary")
    def test_get_operations_summary(
            self,
            function_credit_card_http_account: CreditCardAccountHTTPFixture,
            function_fee_http_operation: FeeOperationHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        query = GetOperationsSummaryQueryTestSchema(account_id=function_credit_card_http_account.id)
        response = operations_gateway_http_test_client.get_operations_summary_api(query)
        response_data = GetOperationsSummaryResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

    @allure.story(AllureStory.GET_OPERATION_RECEIPT)
    @allure.title("[HTTP] Get operation receipt")
    def test_get_operations_receipt(
            self,
            function_credit_card_http_account: CreditCardAccountHTTPFixture,
            function_fee_http_operation: FeeOperationHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        response = operations_gateway_http_test_client.get_operation_receipt_api(function_fee_http_operation.id)
        response_data = GetOperationReceiptResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_OPERATION)
    @allure.title("[HTTP] Get operation")
    def test_get_operation(
            self,
            function_credit_card_http_account: CreditCardAccountHTTPFixture,
            function_fee_http_operation: FeeOperationHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        response = operations_gateway_http_test_client.get_operation_api(function_fee_http_operation.id)
        response_data = GetOperationResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_operation_response(response_data, function_fee_http_operation.response.operation)

        validate_json_schema(response.json(), response_data.model_json_schema())


    @allure.story(AllureStory.MAKE_FEE_OPERATION)
    @allure.title("[HTTP] Make fee operation")
    def test_make_fee_operation(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeFeeOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_fee_operation_api(request)
        response_data = MakeFeeOperationResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_make_fee_operation_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_TOP_UP_OPERATION)
    @allure.title("[HTTP] Make top up operation")
    def test_make_top_up_operation(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeTopUpOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_top_up_operation_api(request)
        response_data = MakeTopUpOperationResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_make_top_up_operation_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_CASHBACK_OPERATION)
    @allure.title("[HTTP] Make cashback operation")
    def test_make_cashback_operation(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeCashbackOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_cashback_operation_api(request)
        response_data = MakeCashbackOperationResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_make_cashback_operation_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_TRANSFER_OPERATION)
    @allure.title("[HTTP] Make transfer operation")
    def test_make_transfer_operation(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeTransferOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_transfer_operation_api(request)
        response_data = MakeTransferOperationResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_make_transfer_operation_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_PURCHASE_OPERATION)
    @allure.title("[HTTP] Make purchase operation")
    def test_make_purchase_operation(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakePurchaseOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_purchase_operation_api(request)
        response_data = MakePurchaseOperationResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_make_purchase_operation_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_BILL_PAYMENT_OPERATION)
    @allure.title("[HTTP] Make bill payment operation")
    def test_make_bill_payment_operation(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeBillPaymentOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_bill_payment_operation_api(request)
        response_data = MakeBillPaymentOperationResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_make_bill_payment_operation_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_CASH_WITHDRAWAL_OPERATION)
    @allure.title("[HTTP] Make cash withdrawal operation")
    def test_make_cash_withdrawal_operation(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeCashWithdrawalOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_cash_withdrawal_operation_api(request)
        response_data = MakeCashWithdrawalOperationResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_make_cash_withdrawal_operation_response(request, response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

