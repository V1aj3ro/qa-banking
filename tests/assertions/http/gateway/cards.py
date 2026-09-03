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
from tests.schema.cards import IssuePhysicalCardResponseTestSchema, CardTestSchema, IssueVirtualCardResponseTestSchema
from tests.tools.date import to_proto_test_datetime, to_proto_test_date
from tests.tools.logger import get_test_logger
from tests.types.cards import CardTestType, CardTestStatus, CardTestPaymentSystem

logger = get_test_logger("CARDS_GATEWAY_ASSERTIONS")

@allure.step("Check card")
def assert_card(actual: CardTestSchema, expected: CardTestSchema):
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
        actual: IssuePhysicalCardResponseTestSchema,
        expected: IssuePhysicalCardResponseTestSchema
) -> None:
    logger.info("Check issue physical card response")

    assert_card(actual.card, expected.card)

@allure.step("Check issue virtual card response")
def assert_issue_virtual_card_response(
        actual: IssueVirtualCardResponseTestSchema,
        expected: IssueVirtualCardResponseTestSchema
) -> None:
    logger.info("Check issue virtual card response")

    assert_card(actual.card, expected.card)

@allure.step("Check issue physical card response. User with active debit card account")
def assert_issue_physical_card_response_user_with_active_debit_card_account(actual: IssuePhysicalCardResponseTestSchema) -> None:
    logger.info("Check issue physical card response. User with active debit card account")

    expected=IssuePhysicalCardResponseTestSchema(card=CardTestSchema(
        id= "96af71f1-5739-4147-bb55-19474c9afa78",
        pin= "123",
        cvv= "321",
        type= CardTestType.PHYSICAL,
        status= CardTestStatus.ACTIVE,
        account_id= "25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
        card_number= "0000000000000000",
        card_holder= "Anton Gomes",
        expiry_date= date(2029,6,27),
        payment_system= CardTestPaymentSystem.MASTERCARD
    ))

    assert_issue_physical_card_response(actual, expected)

@allure.step("Check issue virtual card response. User with one purchase and one top up operations")
def assert_issue_virtual_card_response_user_with_one_purchase_and_one_top_up_operations(actual: IssueVirtualCardResponseTestSchema) -> None:
    logger.info("Check issue virtual card response. User with one purchase and one top up operations")

    expected=IssueVirtualCardResponseTestSchema(card=CardTestSchema(
        id= "ac532047-f67a-4dad-9fe5-3f71a1553cb8",
        pin= "123",
        cvv= "321",
        type= CardTestType.VIRTUAL,
        status= CardTestStatus.ACTIVE,
        account_id= "25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
        card_number= "0000000000000000",
        card_holder= "Anton Gomes",
        expiry_date= date(2029,6,27),
        payment_system= CardTestPaymentSystem.VISA
    ))

    assert_issue_virtual_card_response(actual, expected)