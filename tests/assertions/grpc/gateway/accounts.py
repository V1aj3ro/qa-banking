from datetime import date

import allure

from contracts.services.accounts.account_pb2 import AccountType, AccountStatus
from contracts.services.cards.card_pb2 import Card, CardType, CardStatus, CardPaymentSystem
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
from tests.tools.date import to_proto_test_date
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
    for index, card in enumerate(expected.cards):
        assert_card(actual.cards[index], card)


@allure.step("Check get accounts response")
def assert_get_accounts_response(
        actual: GetAccountsResponse,
        expected: GetAccountsResponse
) -> None:
    logger.info("Check get accounts response")

    assert_length(actual.accounts, expected.accounts, "Accounts list")
    for index, account in enumerate(expected.accounts):
        assert_account(actual.accounts[index], account)

@allure.step("Check open deposit account response")
def assert_open_deposit_account_response(
        actual: OpenDepositAccountResponse,
        expected: OpenDepositAccountResponse
) -> None:
    logger.info("Check open deposit account response")

    assert_account(actual.account, expected.account)

@allure.step("Check open savings account response")
def assert_open_savings_account_response(
        actual: OpenSavingsAccountResponse,
        expected: OpenSavingsAccountResponse
) -> None:
    logger.info("Check open savings account response")

    assert_account(actual.account, expected.account)

@allure.step("Check open debit card account response")
def assert_open_debit_card_account_response(
    actual: OpenDebitCardAccountResponse,
    expected: OpenDebitCardAccountResponse
) -> None:
    logger.info("Check open debit card account response")

    assert_account(actual.account, expected.account)

@allure.step("Check open credit card account response")
def assert_open_credit_card_account_response(
        actual: OpenCreditCardAccountResponse,
        expected: OpenCreditCardAccountResponse
) -> None:
    logger.info("Check open credit card account response")

    assert_account(actual.account, expected.account)

@allure.step("Check get accounts response. User with active debit card account")
def assert_get_accounts_response_user_with_active_debit_card_account(actual: GetAccountsResponse) -> None:
    logger.info("Check get accounts response. User with active debit card account")

    expected=GetAccountsResponse(
        accounts=[
        AccountView(
            id= "25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
            type= AccountType.ACCOUNT_TYPE_DEBIT_CARD,
            cards=[
                Card(
                    id="f0d1aa99-7cc8-4852-940f-bd9eb0ee7681",
                    pin="123",
                    cvv="321",
                    type=CardType.CARD_TYPE_PHYSICAL,
                    status=CardStatus.CARD_STATUS_ACTIVE,
                    accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    cardNumber="0000000000000000",
                    cardHolder="Anton Gomes",
                    expiryDate=to_proto_test_date(date(2029, 6, 27)),
                    paymentSystem=CardPaymentSystem.CARD_PAYMENT_SYSTEM_MASTERCARD,
                ),
                Card(
                    id="f09c4b3c3-1a9b-474d-925f-d543c027ece5",
                    pin="123",
                    cvv="321",
                    type=CardType.CARD_TYPE_VIRTUAL,
                    status=CardStatus.CARD_STATUS_ACTIVE,
                    accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    cardNumber="0000000000000000",
                    cardHolder="Anton Gomes",
                    expiryDate=to_proto_test_date(date(2029, 6, 27)),
                    paymentSystem=CardPaymentSystem.CARD_PAYMENT_SYSTEM_VISA,
                )
            ],
            status= AccountStatus.ACCOUNT_STATUS_ACTIVE,
            balance= 1000
            )
        ]
    )

    assert_get_accounts_response(actual, expected)

@allure.step("Check open credit card account response. User with active debit card account")
def assert_open_credit_card_account_response_user_with_active_debit_card_account(actual: OpenCreditCardAccountResponse) -> None:
    logger.info("Check open credit card account response. User with active debit card account")

    expected=OpenCreditCardAccountResponse(
        account=AccountView(
        id= "76936706-200d-493b-9d80-b9a0b7ebffc2",
        type= AccountType.ACCOUNT_TYPE_CREDIT_CARD,
        cards=[
            Card(
                id="f0d1aa99-7cc8-4852-940f-bd9eb0ee7681",
                pin="123",
                cvv="321",
                type=CardType.CARD_TYPE_PHYSICAL,
                status=CardStatus.CARD_STATUS_ACTIVE,
                accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                cardNumber="0000000000000000",
                cardHolder="Anton Gomes",
                expiryDate=to_proto_test_date(date(2029, 6, 27)),
                paymentSystem=CardPaymentSystem.CARD_PAYMENT_SYSTEM_MASTERCARD,
            ),
            Card(
                id="f09c4b3c3-1a9b-474d-925f-d543c027ece5",
                pin="123",
                cvv="321",
                type=CardType.CARD_TYPE_VIRTUAL,
                status=CardStatus.CARD_STATUS_ACTIVE,
                accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                cardNumber="0000000000000000",
                cardHolder="Anton Gomes",
                expiryDate=to_proto_test_date(date(2029, 6, 27)),
                paymentSystem=CardPaymentSystem.CARD_PAYMENT_SYSTEM_VISA,
            )
        ],
        status= AccountStatus.ACCOUNT_STATUS_ACTIVE,
        balance= 25000
    ))

    assert_open_credit_card_account_response(actual, expected)

@allure.step("Check get accounts response. User with one purchase and one top op operations")
def assert_get_accounts_response_user_with_one_purchase_and_one_top_up_operations(actual: GetAccountsResponse) -> None:
    logger.info("Check get accounts response. User with one purchase and one top op operations")

    expected = GetAccountsResponse(
        accounts = [
        AccountView(
            id="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
            type=AccountType.ACCOUNT_TYPE_DEBIT_CARD,
            cards=[
                Card(
                id="f0d1aa99-7cc8-4852-940f-bd9eb0ee7681",
                pin="123",
                cvv="321",
                type=CardType.CARD_TYPE_PHYSICAL,
                status=CardStatus.CARD_STATUS_ACTIVE,
                accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                cardNumber="0000000000000000",
                cardHolder="Anton Gomes",
                expiryDate=to_proto_test_date(date(2029, 6, 27)),
                paymentSystem=CardPaymentSystem.CARD_PAYMENT_SYSTEM_MASTERCARD,
                ),
                Card(
                    id="f09c4b3c3-1a9b-474d-925f-d543c027ece5",
                    pin="123",
                    cvv="321",
                    type=CardType.CARD_TYPE_VIRTUAL,
                    status=CardStatus.CARD_STATUS_ACTIVE,
                    accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    cardNumber="0000000000000000",
                    cardHolder="Anton Gomes",
                    expiryDate=to_proto_test_date(date(2029, 6, 27)),
                    paymentSystem=CardPaymentSystem.CARD_PAYMENT_SYSTEM_VISA,
                )
            ],
            status=AccountStatus.ACCOUNT_STATUS_ACTIVE,
            balance=12500
        ),
        AccountView(
            id="76936706-200d-493b-9d80-b9a0b7ebffc2",
            type=AccountType.ACCOUNT_TYPE_CREDIT_CARD,
            cards=[
                Card(
                    id="f0d1aa99-7cc8-4852-940f-bd9eb0ee7681",
                    pin="123",
                    cvv="321",
                    type=CardType.CARD_TYPE_PHYSICAL,
                    status=CardStatus.CARD_STATUS_ACTIVE,
                    accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    cardNumber="0000000000000000",
                    cardHolder="Anton Gomes",
                    expiryDate=to_proto_test_date(date(2029, 6, 27)),
                    paymentSystem=CardPaymentSystem.CARD_PAYMENT_SYSTEM_MASTERCARD,
                ),
                Card(
                    id="f09c4b3c3-1a9b-474d-925f-d543c027ece5",
                    pin="123",
                    cvv="321",
                    type=CardType.CARD_TYPE_VIRTUAL,
                    status=CardStatus.CARD_STATUS_ACTIVE,
                    accountId="25e8dcef-cb67-41f1-9fe5-6a6973f4a0e8",
                    cardNumber="0000000000000000",
                    cardHolder="Anton Gomes",
                    expiryDate=to_proto_test_date(date(2029, 6, 27)),
                    paymentSystem=CardPaymentSystem.CARD_PAYMENT_SYSTEM_VISA,
                )
            ],
            status=AccountStatus.ACCOUNT_STATUS_ACTIVE,
            balance=25000
        )
        ]
    )

    assert_get_accounts_response(actual, expected)

@allure.step("Check open deposit account response. User with one purchase and one top op operations")
def assert_open_deposit_account_response_user_with_one_purchase_and_one_top_up_operations(actual: OpenDepositAccountResponse) -> None:
    logger.info("Check open deposit account response. User with one purchase and one top op operations")

    expected = OpenDepositAccountResponse(
        account = AccountView(
            id="c366654e-a231-4309-b965-2c593a54d8f8",
            type=AccountType.ACCOUNT_TYPE_DEPOSIT,
            cards=[],
            status=AccountStatus.ACCOUNT_STATUS_ACTIVE,
            balance=25000
        )
    )

    assert_open_deposit_account_response(actual, expected)