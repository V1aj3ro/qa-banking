from datetime import date

import allure

from contracts.services.cards.card_pb2 import Card, CardType, CardPaymentSystem, CardStatus
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import (
    IssuePhysicalCardResponse,
    IssuePhysicalCardRequest
)
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import (
    IssueVirtualCardResponse,
    IssueVirtualCardRequest
)
from tests.assertions.base import assert_equal
from tests.tools.date import to_proto_test_datetime, to_proto_test_date
from tests.tools.logger import get_test_logger

logger = get_test_logger("CARDS_GATEWAY_ASSERTIONS")

@allure.step("Check card")
def assert_card(actual: Card, expected: Card):
    logger.info("Check card")

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
        actual: IssuePhysicalCardResponse,
        expected: IssuePhysicalCardResponse
) -> None:
    logger.info("Check issue physical card response")

    assert_card(actual.card, expected.card)

@allure.step("Check issue virtual card response")
def assert_issue_virtual_card_response(
        actual: IssueVirtualCardResponse,
        expected: IssueVirtualCardResponse
) -> None:
    logger.info("Check issue virtual card response")

    assert_card(actual.card, expected.card)

@allure.step("Check issue physical card response. User with active debit card account")
def assert_issue_physical_card_response_user_with_active_debit_card_account(actual: IssuePhysicalCardResponse) -> None:
    logger.info("Check issue physical card response. User with active debit card account")

    expected=IssuePhysicalCardResponse(Card(
        id= "96af71f1-5739-4147-bb55-19474c9afa78",
        pin= "123",
        cvv= "321",
        type= CardType.CARD_TYPE_PHYSICAL,
        status= CardStatus.CARD_STATUS_ACTIVE,
        accountId= "25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
        cardNumber= "0000000000000000",
        cardHolder= "Anton Gomes",
        expiryDate= to_proto_test_date(date(2029, 6, 27)),
        paymentSystem= CardPaymentSystem.CARD_PAYMENT_SYSTEM_MASTERCARD
    ))

    assert_issue_physical_card_response(actual, expected)

@allure.step("Check issue virtual card response. User with one purchase and one top up operations")
def assert_issue_virtual_card_response_user_with_one_purchase_and_one_top_up_operations(actual: IssueVirtualCardResponse) -> None:
    logger.info("Check issue virtual card response. User with one purchase and one top up operations")

    expected=IssueVirtualCardResponse(Card(
        id= "ac532047-f67a-4dad-9fe5-3f71a1553cb8",
        pin= "123",
        cvv= "321",
        type= CardType.CARD_TYPE_VIRTUAL,
        status= CardStatus.CARD_STATUS_ACTIVE,
        accountId= "25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
        cardNumber= "0000000000000000",
        cardHolder= "Anton Gomes",
        expiryDate= to_proto_test_date(date(2029, 6, 27)),
        paymentSystem= CardPaymentSystem.CARD_PAYMENT_SYSTEM_MASTERCARD
    ))

    assert_issue_virtual_card_response(actual, expected)