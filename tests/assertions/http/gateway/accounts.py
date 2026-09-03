from datetime import date

import allure

from contracts.services.accounts.account_pb2 import AccountType, AccountStatus
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
from tests.assertions.http.cards import assert_card
from tests.schema.accounts import AccountTestSchema, GetAccountsResponseTestSchema, \
    OpenDepositAccountResponseTestSchema, OpenSavingsAccountResponseTestSchema, OpenDebitCardAccountResponseTestSchema, \
    OpenCreditCardAccountResponseTestSchema
from tests.schema.cards import CardTestSchema
from tests.tools.logger import get_test_logger
from tests.types.accounts import AccountTestType, AccountTestStatus
from tests.types.cards import CardTestType, CardTestStatus, CardTestPaymentSystem

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
        actual: GetAccountsResponseTestSchema,
        expected: GetAccountsResponseTestSchema
) -> None:
    logger.info("Check get accounts response")

    assert_length(actual.accounts, expected.accounts, "Accounts list")
    for index, account in enumerate(expected.accounts):
        assert_account(actual.accounts[index], account)

@allure.step("Check open deposit account response")
def assert_open_deposit_account_response(
        actual: OpenDepositAccountResponseTestSchema,
        expected: OpenDepositAccountResponseTestSchema
) -> None:
    logger.info("Check open deposit account response")

    assert_account(actual.account, expected.account)

@allure.step("Check open savings account response")
def assert_open_savings_account_response(
        actual: OpenSavingsAccountResponseTestSchema,
        expected: OpenSavingsAccountResponseTestSchema
) -> None:
    logger.info("Check open savings account response")

    assert_account(actual.account, expected.account)

@allure.step("Check open debit card account response")
def assert_open_debit_card_account_response(
    actual: OpenDebitCardAccountResponseTestSchema,
    expected: OpenDebitCardAccountResponseTestSchema
) -> None:
    logger.info("Check open debit card account response")

    assert_account(actual.account, expected.account)

@allure.step("Check open credit card account response")
def assert_open_credit_card_account_response(
        actual: OpenCreditCardAccountResponseTestSchema,
        expected: OpenCreditCardAccountResponseTestSchema
) -> None:
    logger.info("Check open credit card account response")

    assert_account(actual.account, expected.account)

@allure.step("Check get accounts response. User with active debit card account")
def assert_get_accounts_response_user_with_active_debit_card_account(actual: GetAccountsResponseTestSchema) -> None:
    logger.info("Check get accounts response. User with active debit card account")

    expected=GetAccountsResponseTestSchema(
        accounts=[
            AccountTestSchema(
            id= "25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
            type= AccountTestType.CREDIT_CARD,
                cards=[
                    CardTestSchema(
                        id="f0d1aa99-7cc8-4852-940f-bd9eb0ee7681",
                        pin="123",
                        cvv="321",
                        type=CardTestType.PHYSICAL,
                        status=CardTestStatus.ACTIVE,
                        account_id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                        card_number="0000000000000000",
                        card_holder="Anton Gomes",
                        expiry_date=date(2029,6,27),
                        payment_system=CardTestPaymentSystem.MASTERCARD,
                    ),
                    CardTestSchema(
                        id="f09c4b3c3-1a9b-474d-925f-d543c027ece5",
                        pin="123",
                        cvv="321",
                        type=CardTestType.VIRTUAL,
                        status=CardTestStatus.ACTIVE,
                        account_id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                        card_number="0000000000000000",
                        card_holder="Anton Gomes",
                        expiry_date=date(2029,6,27),
                        payment_system=CardTestPaymentSystem.VISA,
                    )
                ],
            status=AccountTestStatus.ACTIVE,
            balance= 1000
            )
        ]
    )

    assert_get_accounts_response(actual, expected)

@allure.step("Check open credit card account response. User with active debit card account")
def assert_open_credit_card_account_response_user_with_active_debit_card_account(actual: OpenCreditCardAccountResponseTestSchema) -> None:
    logger.info("Check open credit card account response. User with active debit card account")

    expected=OpenCreditCardAccountResponseTestSchema(
        account=AccountTestSchema(
        id= "76936706-200d-493b-9d80-b9a0b7ebffc2",
        type= AccountTestType.CREDIT_CARD,
        cards=[
            CardTestSchema(
                id="f0d1aa99-7cc8-4852-940f-bd9eb0ee7681",
                pin="123",
                cvv="321",
                type=CardTestType.PHYSICAL,
                status=CardTestStatus.ACTIVE,
                account_id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                card_number="0000000000000000",
                card_holder="Anton Gomes",
                expiry_date=date(2029,6,27),
                payment_system=CardTestPaymentSystem.MASTERCARD,
            ),
            CardTestSchema(
                id="f09c4b3c3-1a9b-474d-925f-d543c027ece5",
                pin="123",
                cvv="321",
                type=CardTestType.VIRTUAL,
                status=CardTestStatus.ACTIVE,
                account_id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                card_number="0000000000000000",
                card_holder="Anton Gomes",
                expiry_date=date(2029,6,27),
                payment_system=CardTestPaymentSystem.VISA,
            )
        ],
        status= AccountTestStatus.ACTIVE,
        balance= 25000
    ))

    assert_open_credit_card_account_response(actual, expected)

@allure.step("Check get accounts response. User with one purchase and one top op operations")
def assert_get_accounts_response_user_with_one_purchase_and_one_top_up_operations(actual: GetAccountsResponseTestSchema) -> None:
    logger.info("Check get accounts response. User with one purchase and one top op operations")

    expected = GetAccountsResponseTestSchema(
        accounts = [
        AccountTestSchema(
            id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
            type=AccountTestType.DEBIT_CARD,
            cards=[
                CardTestSchema(
                    id="f0d1aa99-7cc8-4852-940f-bd9eb0ee7681",
                    pin="123",
                    cvv="321",
                    type=CardTestType.PHYSICAL,
                    status=CardTestStatus.ACTIVE,
                    account_id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    card_number="0000000000000000",
                    card_holder="Anton Gomes",
                    expiry_date=date(2029,6,27),
                    payment_system=CardTestPaymentSystem.MASTERCARD,
                ),
                CardTestSchema(
                    id="f09c4b3c3-1a9b-474d-925f-d543c027ece5",
                    pin="123",
                    cvv="321",
                    type=CardTestType.VIRTUAL,
                    status=CardTestStatus.ACTIVE,
                    account_id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    card_number="0000000000000000",
                    card_holder="Anton Gomes",
                    expiry_date=date(2029,6,27),
                    payment_system=CardTestPaymentSystem.VISA,
                )
            ],
            status=AccountTestStatus.ACTIVE,
            balance=12500
        ),
        AccountTestSchema(
            id="76936706-200d-493b-9d80-b9a0b7ebffc2",
            type=AccountType.ACCOUNT_TYPE_CREDIT_CARD,
            cards=[
                CardTestSchema(
                    id="f0d1aa99-7cc8-4852-940f-bd9eb0ee7681",
                    pin="123",
                    cvv="321",
                    type=CardTestType.PHYSICAL,
                    status=CardTestStatus.ACTIVE,
                    account_id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    card_number="0000000000000000",
                    card_holder="Anton Gomes",
                    expiry_date=date(2029,6,27),
                    payment_system=CardTestPaymentSystem.MASTERCARD,
                ),
                CardTestSchema(
                    id="f09c4b3c3-1a9b-474d-925f-d543c027ece5",
                    pin="123",
                    cvv="321",
                    type=CardTestType.VIRTUAL,
                    status=CardTestStatus.ACTIVE,
                    account_id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    card_number="0000000000000000",
                    card_holder="Anton Gomes",
                    expiry_date=date(2029,6,27),
                    payment_system=CardTestPaymentSystem.VISA,
                )
            ],
            status=AccountTestStatus.ACTIVE,
            balance=25000
        )
        ]
    )

    assert_get_accounts_response(actual, expected)

@allure.step("Check open deposit account response. User with one purchase and one top op operations")
def assert_open_deposit_account_response_user_with_one_purchase_and_one_top_up_operations(actual: OpenDepositAccountResponseTestSchema) -> None:
    logger.info("Check open deposit account response. User with one purchase and one top op operations")

    expected = OpenDepositAccountResponseTestSchema(
        account = AccountTestSchema(
            id="c366654e-a231-4309-b965-2c593a54d8f8",
            type=AccountTestType.DEPOSIT,
            cards=[
                CardTestSchema(
                    id="f0d1aa99-7cc8-4852-940f-bd9eb0ee7681",
                    pin="123",
                    cvv="321",
                    type=CardTestType.PHYSICAL,
                    status=CardTestStatus.ACTIVE,
                    account_id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    card_number="0000000000000000",
                    card_holder="Anton Gomes",
                    expiry_date=date(2029,6,27),
                    payment_system=CardTestPaymentSystem.MASTERCARD,
                ),
                CardTestSchema(
                    id="f09c4b3c3-1a9b-474d-925f-d543c027ece5",
                    pin="123",
                    cvv="321",
                    type=CardTestType.VIRTUAL,
                    status=CardTestStatus.ACTIVE,
                    account_id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    card_number="0000000000000000",
                    card_holder="Anton Gomes",
                    expiry_date=date(2029,6,27),
                    payment_system=CardTestPaymentSystem.VISA,
                )
            ],
            status=AccountTestStatus.ACTIVE,
            balance=25000
        )
    )

    assert_open_deposit_account_response(actual, expected)