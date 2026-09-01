import allure

from tests.assertions.base import assert_equal, assert_length
from tests.assertions.http.cards import assert_card
from tests.schema.accounts import AccountTestSchema, GetAccountsResponseTestSchema, \
    OpenDebitCardAccountResponseTestSchema, OpenDepositAccountResponseTestSchema, OpenSavingsAccountResponseTestSchema, \
    OpenCreditCardAccountResponseTestSchema
from tests.schema.users import CreateUserResponseTestSchema
from tests.types.accounts import AccountTestType


@allure.step("Check account")
def assert_account(actual: AccountTestSchema, expected: AccountTestSchema) -> None:

    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.type, expected.type, "type")
    assert_equal(actual.status, expected.status, "status")
    assert_equal(actual.user_id, expected.user_id, "user_id")
    assert_equal(actual.balance, expected.balance, "balance")

    assert_length(actual.cards, expected.cards, "accounts cards")
    for index, card in enumerate(expected.cards):
        assert_card(actual.cards[index], card)


@allure.step("Check get accounts response")
def assert_get_accounts_response(
        get_accounts_response: GetAccountsResponseTestSchema,
        open_accounts_responses: list[AccountTestSchema]
) -> None:
    assert_length(get_accounts_response.accounts, open_accounts_responses, "Accounts list")
    for index, account in enumerate(open_accounts_responses):
        assert_account(get_accounts_response.accounts[index], account)

@allure.step("Check open deposit account response")
def assert_open_deposit_account_response(
        open_deposit_account_response: OpenDepositAccountResponseTestSchema,
        create_user_response: CreateUserResponseTestSchema
) -> None:
    assert_equal(open_deposit_account_response.account.type, AccountTestType.DEPOSIT, "Account type")
    assert_equal(open_deposit_account_response.account.user_id, create_user_response.user.id, "User id")

@allure.step("Check open savings account response")
def assert_open_savings_account_response(
        open_savings_account_response: OpenSavingsAccountResponseTestSchema,
        create_user_response: CreateUserResponseTestSchema
) -> None:
    assert_equal(open_savings_account_response.account.type, AccountTestType.SAVINGS, "Account type")
    assert_equal(open_savings_account_response.account.user_id, create_user_response.user.id, "User id")

@allure.step("Check open debit card account response")
def assert_open_debit_card_account_response(
        open_debit_card_account_response: OpenDebitCardAccountResponseTestSchema,
        create_user_response: CreateUserResponseTestSchema
) -> None:
    assert_equal(open_debit_card_account_response.account.type, AccountTestType.DEBIT_CARD, "Account type")
    assert_equal(open_debit_card_account_response.account.user_id, create_user_response.user.id, "User id")

@allure.step("Check open credit card account response")
def assert_open_credit_card_account_response(
        open_credit_card_account_response: OpenCreditCardAccountResponseTestSchema,
        create_user_response: CreateUserResponseTestSchema
) -> None:
    assert_equal(open_credit_card_account_response.account.type, AccountTestType.CREDIT_CARD, "Account type")
    assert_equal(open_credit_card_account_response.account.user_id, create_user_response.user.id, "User id")