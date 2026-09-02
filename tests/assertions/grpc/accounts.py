import allure

from contracts.services.accounts.account_pb2 import AccountType
from contracts.services.gateway.accounts.account_pb2 import AccountView
from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import GetAccountsResponse
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountResponse,
    OpenCreditCardAccountRequest
)
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountResponse,
    OpenDebitCardAccountRequest
)
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import (
    OpenDepositAccountResponse,
    OpenDepositAccountRequest
)
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import (
    OpenSavingsAccountResponse,
    OpenSavingsAccountRequest
)
from tests.assertions.base import assert_equal, assert_length
from tests.assertions.grpc.cards import assert_card
from tests.tools.logger import get_test_logger

logger = get_test_logger("ACCOUNTS_GATEWAY_ASSERTIONS")


@allure.step("Check account")
def assert_account(actual: AccountView, expected: AccountView) -> None:
    logger.info("Check account")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.status, expected.status, "status")
    assert_equal(actual.balance, expected.balance, "balance")

    assert_length(actual.cards, expected.cards, "accounts cards")
    actual_cards = sorted(actual.cards, key=lambda c: c.id)
    expected_cards = sorted(expected.cards, key=lambda c: c.id)
    for index, card in enumerate(expected_cards):
        assert_card(actual_cards[index], card)


@allure.step("Check get accounts response")
def assert_get_accounts_response(
        get_accounts_response: GetAccountsResponse,
        open_accounts_responses: list[AccountView]
) -> None:
    logger.info("Check get accounts response")

    assert_length(get_accounts_response.accounts, open_accounts_responses, "Accounts list")
    for index, account in enumerate(open_accounts_responses):
        assert_account(get_accounts_response.accounts[index], account)

@allure.step("Check open deposit account response")
def assert_open_deposit_account_response(
        open_deposit_account_response: OpenDepositAccountResponse,
        open_deposit_account_request: OpenDepositAccountRequest
) -> None:
    logger.info("Check open deposit account response")

    assert_equal(open_deposit_account_response.account.type, AccountType.ACCOUNT_TYPE_DEPOSIT, "Account type")

@allure.step("Check open savings account response")
def assert_open_savings_account_response(
        open_savings_account_response: OpenSavingsAccountResponse,
        open_savings_account_request: OpenSavingsAccountRequest
) -> None:
    logger.info("Check open savings account response")

    assert_equal(open_savings_account_response.account.type, AccountType.ACCOUNT_TYPE_SAVINGS, "Account type")

@allure.step("Check open debit card account response")
def assert_open_debit_card_account_response(
    open_debit_card_account_response: OpenDebitCardAccountResponse,
    open_debit_card_account_request: OpenDebitCardAccountRequest
) -> None:
    logger.info("Check open debit card account response")

    assert_equal(open_debit_card_account_response.account.type, AccountType.ACCOUNT_TYPE_DEBIT_CARD, "Account type")

@allure.step("Check open credit card account response")
def assert_open_credit_card_account_response(
        open_credit_card_account_response: OpenCreditCardAccountResponse,
        open_credit_card_account_request: OpenCreditCardAccountRequest
) -> None:
    logger.info("Check open credit card account response")

    assert_equal(open_credit_card_account_response.account.type, AccountType.ACCOUNT_TYPE_CREDIT_CARD, "Account type")