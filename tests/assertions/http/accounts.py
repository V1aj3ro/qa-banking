import allure

from tests.assertions.base import assert_equal, assert_length
from tests.assertions.http.cards import assert_card
from tests.schema.accounts import (
    AccountTestSchema,
    GetAccountsResponseTestSchema,
    OpenDebitCardAccountResponseTestSchema,
    OpenDepositAccountResponseTestSchema,
    OpenSavingsAccountResponseTestSchema,
    OpenCreditCardAccountResponseTestSchema,
    OpenDebitCardAccountRequestTestSchema,
    OpenCreditCardAccountRequestTestSchema,
    OpenSavingsAccountRequestTestSchema,
    OpenDepositAccountRequestTestSchema
)
from tests.tools.logger import get_test_logger
from tests.types.accounts import AccountTestType

logger = get_test_logger("ACCOUNTS_GATEWAY_ASSERTIONS")


@allure.step("Check account")
def assert_account(actual: AccountTestSchema, expected: AccountTestSchema) -> None:
    logger.info("Check account")

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.status, expected.status, "status")
    assert_equal(actual.balance, expected.balance, "balance")

    assert_length(actual.cards, expected.cards, "accounts cards")
    for index, card in enumerate(expected.cards):
        assert_card(actual.cards[index], card)


@allure.step("Check get accounts response")
def assert_get_accounts_response(
        get_accounts_response: GetAccountsResponseTestSchema,
        open_accounts_responses: list[AccountTestSchema]
) -> None:
    logger.info("Check get accounts response")

    assert_length(get_accounts_response.accounts, open_accounts_responses, "Accounts list")
    for index, account in enumerate(open_accounts_responses):
        assert_account(get_accounts_response.accounts[index], account)

@allure.step("Check open deposit account response")
def assert_open_deposit_account_response(
        open_deposit_account_response: OpenDepositAccountResponseTestSchema,
        open_deposit_account_request: OpenDepositAccountRequestTestSchema
) -> None:
    logger.info("Check open deposit account response")

    assert_equal(open_deposit_account_response.account.type, AccountTestType.DEPOSIT, "Account type")

@allure.step("Check open savings account response")
def assert_open_savings_account_response(
        open_savings_account_response: OpenSavingsAccountResponseTestSchema,
        open_savings_account_request: OpenSavingsAccountRequestTestSchema
) -> None:
    logger.info("Check open savings account response")

    assert_equal(open_savings_account_response.account.type, AccountTestType.SAVINGS, "Account type")

@allure.step("Check open debit card account response")
def assert_open_debit_card_account_response(
    open_debit_card_account_response: OpenDebitCardAccountResponseTestSchema,
    open_debit_card_account_request: OpenDebitCardAccountRequestTestSchema
) -> None:
    logger.info("Check open debit card account response")

    assert_equal(open_debit_card_account_response.account.type, AccountTestType.DEBIT_CARD, "Account type")

@allure.step("Check open credit card account response")
def assert_open_credit_card_account_response(
        open_credit_card_account_response: OpenCreditCardAccountResponseTestSchema,
        open_credit_card_account_request: OpenCreditCardAccountRequestTestSchema
) -> None:
    logger.info("Check open credit card account response")

    assert_equal(open_credit_card_account_response.account.type, AccountTestType.CREDIT_CARD, "Account type")