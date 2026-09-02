import allure

from contracts.services.cards.card_pb2 import Card, CardType
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import (
    IssuePhysicalCardResponse,
    IssuePhysicalCardRequest
)
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import (
    IssueVirtualCardResponse,
    IssueVirtualCardRequest
)
from tests.assertions.base import assert_equal
from tests.tools.logger import get_test_logger

logger = get_test_logger("CARDS_GATEWAY_ASSERTIONS")

@allure.step("Check card")
def assert_card(actual: Card, expected: Card):
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

@allure.step("Check issue physical card response")
def assert_issue_physical_card_response(
        issue_physical_card_response: IssuePhysicalCardResponse,
        issue_physical_card_request: IssuePhysicalCardRequest
) -> None:
    logger.info("Check issue physical card response")

    assert_equal(issue_physical_card_response.card.type, CardType.CARD_TYPE_PHYSICAL, "Card type")
    assert_equal(issue_physical_card_response.card.account_id, issue_physical_card_request.account_id, "Account id")

@allure.step("Check issue virtual card response")
def assert_issue_virtual_card_response(
        issue_virtual_card_response: IssueVirtualCardResponse,
        issue_virtual_card_request: IssueVirtualCardRequest
) -> None:
    logger.info("Check issue virtual card response")

    assert_equal(issue_virtual_card_response.card.type, CardType.CARD_TYPE_VIRTUAL, "Card type")
    assert_equal(issue_virtual_card_response.card.account_id, issue_virtual_card_request.account_id, "Account id")
