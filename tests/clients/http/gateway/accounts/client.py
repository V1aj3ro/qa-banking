from typing import Optional

import allure
from httpx import Response, QueryParams

from tests.clients.http.api_coverage import tracker
from tests.clients.http.client import HTTPTestClient
from tests.clients.http.gateway.client import build_gateway_http_test_client
from tests.context.base import RequestContext
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
from tests.tools.fakers import fake
from tests.tools.logger import get_test_logger
from tests.tools.routes import APITestRoutes


class AccountsGatewayHTTPTestClient(HTTPTestClient):
    @allure.step("Get accounts")
    @tracker.track_coverage_httpx(APITestRoutes.ACCOUNTS)
    def get_accounts_api(self, query: GetAccountsQueryTestSchema, context: Optional[RequestContext] = None) -> Response:
        return self.get(
            APITestRoutes.ACCOUNTS,
            params=QueryParams(**query.model_dump(by_alias=True)),
            context=context
        )

    @allure.step("Open deposit account")
    @tracker.track_coverage_httpx(f"{APITestRoutes.ACCOUNTS}/open-deposit-account")
    def open_deposit_account_api(
            self,
            request: OpenDepositAccountRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.ACCOUNTS}/open-deposit-account",
            json=request.model_dump(by_alias=True),
            context=context
        )

    @allure.step("Open savings account")
    @tracker.track_coverage_httpx(f"{APITestRoutes.ACCOUNTS}/open-savings-account")
    def open_savings_account_api(
            self,
            request: OpenSavingsAccountRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.ACCOUNTS}/open-savings-account",
            json=request.model_dump(by_alias=True),
            context=context
        )

    @allure.step("Open debit card account")
    @tracker.track_coverage_httpx(f"{APITestRoutes.ACCOUNTS}/open-debit-card-account")
    def open_debit_card_account_api(
            self,
            request: OpenDebitCardAccountRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.ACCOUNTS}/open-debit-card-account",
            json=request.model_dump(by_alias=True),
            context=context
        )

    @allure.step("Open credit card account")
    @tracker.track_coverage_httpx(f"{APITestRoutes.ACCOUNTS}/open-credit-card-account")
    def open_credit_card_account_api(
            self,
            request: OpenCreditCardAccountRequestTestSchema,
            context: Optional[RequestContext] = None
    ) -> Response:
        return self.post(
            f"{APITestRoutes.ACCOUNTS}/open-credit-card-account",
            json=request.model_dump(by_alias=True),
            context=context
        )

    def get_accounts(
            self,
            query: Optional[GetAccountsQueryTestSchema],
            context: Optional[RequestContext] = None
    ) -> GetAccountsResponseTestSchema:
        if query is None:
            query = GetAccountsQueryTestSchema(user_id=fake.uuid())
        response = self.get_accounts_api(query, context)
        return GetAccountsResponseTestSchema.model_validate_json(response.text)

    def open_deposit_account(
            self,
            request: Optional[OpenDepositAccountRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> OpenDepositAccountResponseTestSchema:
        if request is None:
            request = OpenDepositAccountRequestTestSchema(user_id=fake.uuid())
        response = self.open_deposit_account_api(request, context)
        return OpenDepositAccountResponseTestSchema.model_validate_json(response.text)

    def open_savings_account(
            self,
            request: Optional[OpenSavingsAccountRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> OpenSavingsAccountResponseTestSchema:
        if request is None:
            request = OpenSavingsAccountRequestTestSchema(user_id=fake.uuid())
        response = self.open_savings_account_api(request, context)
        return OpenSavingsAccountResponseTestSchema.model_validate_json(response.text)

    def open_debit_card_account(
            self,
            request: Optional[OpenDebitCardAccountRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> OpenDebitCardAccountResponseTestSchema:
        if request is None:
            request = OpenDebitCardAccountRequestTestSchema(user_id=fake.uuid())
        response = self.open_debit_card_account_api(request, context)
        return OpenDebitCardAccountResponseTestSchema.model_validate_json(response.text)

    def open_credit_card_account(
            self,
            request: Optional[OpenCreditCardAccountRequestTestSchema],
            context: Optional[RequestContext] = None
    ) -> OpenCreditCardAccountResponseTestSchema:
        if request is None:
            request = OpenCreditCardAccountRequestTestSchema(user_id=fake.uuid())
        response = self.open_credit_card_account_api(request, context)
        return OpenCreditCardAccountResponseTestSchema.model_validate_json(response.text)


def build_accounts_gateway_http_test_client() -> AccountsGatewayHTTPTestClient:
    return AccountsGatewayHTTPTestClient(client=build_gateway_http_test_client(
        logger=get_test_logger("ACCOUNTS_GATEWAY_HTTP_TEST_CLIENT")
        )
    )

