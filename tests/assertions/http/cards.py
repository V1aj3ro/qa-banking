import allure

from tests.assertions.base import assert_equal
from tests.schema.cards import CardTestSchema


@allure.step("Check card")
def assert_card(actual: CardTestSchema, expected: CardTestSchema):
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.account_id, expected.account_id, "account_id")
    assert_equal(actual.status, expected.status, "status")
    assert_equal(actual.card_holder, expected.card_holder, "card_holder")
    assert_equal(actual.card_number, expected.card_number, "card_number")
    assert_equal(actual.cvv, expected.cvv, "cvv")
    assert_equal(actual.expiry_date, expected.expiry_date, "expiry_date")
    assert_equal(actual.payment_system, expected.payment_system, "payment_system")
    assert_equal(actual.pin, expected.pin, "pin")
    assert_equal(actual.type, expected.type, "type")

