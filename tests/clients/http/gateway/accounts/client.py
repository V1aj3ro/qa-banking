import allure
from httpx import Response, QueryParams

from tests.clients.http.client import HTTPTestClient
from tests.clients.http.gateway.client import build_gateway_http_test_client
from tests.schema.accounts import (
    GetAccountsQueryTestSchema,
    GetAccountsResponseTestSchema,
    OpenCreditCardAccountRequestTestSchema,
    OpenCreditCardAccountResponseTestSchema,
    OpenDebitCardAccountRequestTestSchema,
    OpenDebitCardAccountResponseTestSchema,
    OpenDepositAccountRequestTestSchema,
    OpenDepositAccountResponseTestSchema,
    OpenSavingsAccountRequestTestSchema,
    OpenSavingsAccountResponseTestSchema,

)
from tests.tools.logger import get_test_logger
from tests.tools.routes import APITestRoutes


class AccountsGatewayHTTPTestClient(HTTPTestClient):
    @allure.step("Get accounts")
    def get_accounts_api(self, query: GetAccountsQueryTestSchema):
        return self.get(
            APITestRoutes.ACCOUNTS,
            params=QueryParams(**query.model_dump(by_alias=True)),
        )

    @allure.step("Open deposit account")
    def open_deposit_account_api(self, request: OpenDepositAccountRequestTestSchema) -> Response:
        return self.post(
            f"{APITestRoutes.ACCOUNTS}/open-deposit-account",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Open savings account")
    def open_savings_account_api(self, request: OpenSavingsAccountRequestTestSchema) -> Response:
        return self.post(
            f"{APITestRoutes.ACCOUNTS}/open-savings-account",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Open debit card account")
    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestTestSchema) -> Response:
        return self.post(
            f"{APITestRoutes.ACCOUNTS}/open-debit-card-account",
            json=request.model_dump(by_alias=True)
        )

    @allure.step("Open credit card account")
    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestTestSchema) -> Response:
        return self.post(
            f"{APITestRoutes.ACCOUNTS}/open-credit-card-account",
            json=request.model_dump(by_alias=True)
        )

    def get_accounts(self, user_id: str) -> GetAccountsResponseTestSchema:
        query = GetAccountsQueryTestSchema(user_id=user_id)
        response = self.get_accounts_api(query)
        return GetAccountsResponseTestSchema.model_validate_json(response.text)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseTestSchema:
        request = OpenDepositAccountRequestTestSchema(user_id=user_id)
        response = self.open_deposit_account_api(request)
        return OpenDepositAccountResponseTestSchema.model_validate_json(response.text)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponseTestSchema:
        request = OpenSavingsAccountRequestTestSchema(user_id=user_id)
        response = self.open_savings_account_api(request)
        return OpenSavingsAccountResponseTestSchema.model_validate_json(response.text)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseTestSchema:
        request = OpenDebitCardAccountRequestTestSchema(user_id=user_id)
        response = self.open_debit_card_account_api(request)
        return OpenDebitCardAccountResponseTestSchema.model_validate_json(response.text)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseTestSchema:
        request = OpenCreditCardAccountRequestTestSchema(user_id=user_id)
        response = self.open_credit_card_account_api(request)
        return OpenCreditCardAccountResponseTestSchema.model_validate_json(response.text)


def build_accounts_gateway_http_test_client() -> AccountsGatewayHTTPTestClient:
    return AccountsGatewayHTTPTestClient(client=build_gateway_http_test_client(
        logger=get_test_logger("ACCOUNTS_GATEWAY_HTTP_TEST_CLIENT")
        )
    )

