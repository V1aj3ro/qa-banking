import allure

from tests.assertions.base import assert_equal, assert_length
from tests.assertions.http.cards import assert_card
from tests.schema.accounts import AccountTestSchema, GetAccountsResponseTestSchema


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
