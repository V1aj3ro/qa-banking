from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.operations import (
    assert_get_operations_response_with_incorrect_account_id,
    assert_get_operations_summary_response_with_incorrect_account_id,
    assert_get_operation_receipt_response_with_incorrect_operation_id,
    assert_get_operation_response_with_incorrect_operation_id, assert_make_operation_response_with_incorrect_card_id,
    assert_make_operation_response_with_incorrect_account_id,
    assert_make_operation_response_with_incorrect_card_id_and_account_id
)
from tests.assertions.http.schema import validate_json_schema
from tests.clients.http.gateway.operations.client import OperationsGatewayHTTPTestClient
from tests.fixtures.http.gateway.accounts.schema import (
    DepositAccountHTTPFixture,
)
from tests.fixtures.http.gateway.cards.fixtures import function_virtual_http_card
from tests.fixtures.http.gateway.cards.schema import VirtualCardHTTPFixture
from tests.schema.errors import ValidationErrorResponseSchema
from tests.schema.operations import (
    MakeFeeOperationRequestTestSchema,
    MakeTopUpOperationRequestTestSchema,
    MakeCashbackOperationRequestTestSchema,
    MakeTransferOperationRequestTestSchema,
    MakePurchaseOperationRequestTestSchema,
    MakeBillPaymentOperationRequestTestSchema,
    MakeCashWithdrawalOperationRequestTestSchema,
    GetOperationsQueryTestSchema,
    GetOperationsSummaryQueryTestSchema
)
from tests.tools.allure import AllureTag, AllureEpic, AllureFeature, AllureStory


@pytest.mark.gateway
@pytest.mark.gateway_operations
@pytest.mark.regression
@pytest.mark.negative
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE, AllureTag.NEGATIVE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.OPERATIONS_GATEWAY_SERVICE)
class TestOperationsNegativeHTTP:
    @allure.story(AllureStory.GET_OPERATIONS)
    @allure.title("[HTTP] Get operations with incorrect account id")
    def test_get_operations_with_incorrect_account_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        query = GetOperationsQueryTestSchema(account_id="incorrect-account-id")
        response = operations_gateway_http_test_client.get_operations_api(query)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_operations_response_with_incorrect_account_id(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_OPERATIONS)
    @allure.title("[HTTP] Get operations summary with incorrect account id")
    def test_get_operations_summary_with_incorrect_account_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        query = GetOperationsSummaryQueryTestSchema(account_id="incorrect-account-id")
        response = operations_gateway_http_test_client.get_operations_summary_api(query)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_operations_summary_response_with_incorrect_account_id(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_OPERATIONS)
    @allure.title("[HTTP] Get operation receipt with incorrect operation id")
    def test_get_operation_receipt_with_incorrect_operation_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        response = operations_gateway_http_test_client.get_operation_receipt_api(operation_id="incorrect-operation-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_operation_receipt_response_with_incorrect_operation_id(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_OPERATIONS)
    @allure.title("[HTTP] Get operation with incorrect operation id")
    def test_get_operation_with_incorrect_operation_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        response = operations_gateway_http_test_client.get_operation_api(operation_id="incorrect-operation-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_operation_response_with_incorrect_operation_id(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_FEE_OPERATION)
    @allure.title("[HTTP] Make fee operation with incorrect card id")
    def test_make_fee_operation_with_incorrect_card_id(
            self,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeFeeOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_fee_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_FEE_OPERATION)
    @allure.title("[HTTP] Make fee operation with incorrect account id")
    def test_make_fee_operation_with_incorrect_account_id(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeFeeOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_fee_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_FEE_OPERATION)
    @allure.title("[HTTP] Make fee operation with incorrect card id and account id")
    def test_make_fee_operation_with_incorrect_card_id_and_account_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeFeeOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_fee_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id_and_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_TOP_UP_OPERATION)
    @allure.title("[HTTP] Make top up operation with incorrect card id")
    def test_make_top_up_operation_with_incorrect_card_id(
            self,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeTopUpOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_top_up_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_TOP_UP_OPERATION)
    @allure.title("[HTTP] Make top up operation with incorrect account id")
    def test_make_top_up_operation_with_incorrect_account_id(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeTopUpOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_top_up_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_TOP_UP_OPERATION)
    @allure.title("[HTTP] Make top up operation with incorrect card id and account id")
    def test_make_top_up_operation_with_incorrect_card_id_and_account_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeTopUpOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_top_up_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id_and_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_CASHBACK_OPERATION)
    @allure.title("[HTTP] Make cashback operation with incorrect card id")
    def test_make_cashback_operation_with_incorrect_card_id(
            self,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeCashbackOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_cashback_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_CASHBACK_OPERATION)
    @allure.title("[HTTP] Make cashback operation with incorrect account id")
    def test_make_cashback_operation_with_incorrect_account_id(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeCashbackOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_cashback_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_CASHBACK_OPERATION)
    @allure.title("[HTTP] Make cashback operation with incorrect card id and account id")
    def test_make_cashback_operation_with_incorrect_card_id_and_account_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeCashbackOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_cashback_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id_and_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_TRANSFER_OPERATION)
    @allure.title("[HTTP] Make transfer operation with incorrect card id")
    def test_make_transfer_operation_with_incorrect_card_id(
            self,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeTransferOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_transfer_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_TRANSFER_OPERATION)
    @allure.title("[HTTP] Make transfer operation with incorrect account id")
    def test_make_transfer_operation_with_incorrect_account_id(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeTransferOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_transfer_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_TRANSFER_OPERATION)
    @allure.title("[HTTP] Make transfer operation with incorrect card id and account id")
    def test_make_transfer_operation_with_incorrect_card_id_and_account_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeTransferOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_transfer_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id_and_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_PURCHASE_OPERATION)
    @allure.title("[HTTP] Make purchase operation with incorrect card id")
    def test_make_purchase_operation_with_incorrect_card_id(
            self,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakePurchaseOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_purchase_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_PURCHASE_OPERATION)
    @allure.title("[HTTP] Make purchase operation with incorrect account id")
    def test_make_purchase_operation_with_incorrect_account_id(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakePurchaseOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_purchase_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_PURCHASE_OPERATION)
    @allure.title("[HTTP] Make purchase operation with incorrect card id and account id")
    def test_make_purchase_operation_with_incorrect_card_id_and_account_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakePurchaseOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_purchase_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id_and_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_BILL_PAYMENT_OPERATION)
    @allure.title("[HTTP] Make bill payment operation with incorrect card id")
    def test_make_bill_payment_operation_with_incorrect_card_id(
            self,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeBillPaymentOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_bill_payment_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_BILL_PAYMENT_OPERATION)
    @allure.title("[HTTP] Make bill payment operation with incorrect account id")
    def test_make_bill_payment_operation_with_incorrect_account_id(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeBillPaymentOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_bill_payment_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_BILL_PAYMENT_OPERATION)
    @allure.title("[HTTP] Make bill payment operation with incorrect card id and account id")
    def test_make_bill_payment_operation_with_incorrect_card_id_and_account_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeBillPaymentOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_bill_payment_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id_and_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_CASH_WITHDRAWAL_OPERATION)
    @allure.title("[HTTP] Make cash withdrawal operation with incorrect card id")
    def test_make_cash_withdrawal_operation_with_incorrect_card_id(
            self,
            function_deposit_http_account: DepositAccountHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeCashWithdrawalOperationRequestTestSchema(
            account_id=function_deposit_http_account.id,
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_cash_withdrawal_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_CASH_WITHDRAWAL_OPERATION)
    @allure.title("[HTTP] Make cash withdrawal operation with incorrect account id")
    def test_make_cash_withdrawal_operation_with_incorrect_account_id(
            self,
            function_virtual_http_card: VirtualCardHTTPFixture,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeCashWithdrawalOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id=function_virtual_http_card.id
        )
        response = operations_gateway_http_test_client.make_cash_withdrawal_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.MAKE_CASH_WITHDRAWAL_OPERATION)
    @allure.title("[HTTP] Make cash withdrawal operation with incorrect card id and account id")
    def test_make_cash_withdrawal_operation_with_incorrect_card_id_and_account_id(
            self,
            operations_gateway_http_test_client: OperationsGatewayHTTPTestClient
    ):
        request = MakeCashWithdrawalOperationRequestTestSchema(
            account_id="incorrect-account-id",
            card_id="incorrect-card-id"
        )
        response = operations_gateway_http_test_client.make_cash_withdrawal_operation_api(request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_make_operation_response_with_incorrect_card_id_and_account_id(response_data)
        validate_json_schema(response.json(), response_data.model_json_schema())
