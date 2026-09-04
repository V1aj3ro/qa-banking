from enum import StrEnum


class AllureTag(StrEnum):
    GRPC = "GRPC"
    HTTP = "HTTP"
    KAFKA = "KAFKA"
    POSTGRES = "POSTGRES"

    GATEWAY_SERVICE = "GATEWAY_SERVICE"
    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"


class AllureStory(StrEnum):
    GET_ACCOUNTS = "Get Accounts"
    OPEN_DEPOSIT_ACCOUNT = "Open Deposit Account"
    OPEN_SAVINGS_ACCOUNT = "Open Savings Account"
    OPEN_DEBIT_CARD_ACCOUNT = "Open Debit Card Account"
    OPEN_CREDIT_CARD_ACCOUNT = "Open Credit Card Account"
    ISSUE_VIRTUAL_CARD = "Issue Virtual Card"
    ISSUE_PHYSICAL_CARD = "Issue Physical Card"
    GET_TARIFF_DOCUMENT = "Get Tariff Document"
    GET_CONTRACT_DOCUMENT = "Get Contract Document"
    GET_OPERATIONS = "Get Operations"
    GET_OPERATIONS_SUMMARY = "Get Operations Summary"
    GET_OPERATION_RECEIPT = "Get Operation Receipt"
    GET_OPERATION = "Get Operation"
    MAKE_FEE_OPERATION = "Make Fee Operation"
    MAKE_TOP_UP_OPERATION = "Make Top up Operation"
    MAKE_CASHBACK_OPERATION = "Make Cashback Operation"
    MAKE_TRANSFER_OPERATION = "Make Transfer Operation"
    MAKE_PURCHASE_OPERATION = "Make Purchase Operation"
    MAKE_BILL_PAYMENT_OPERATION = "Make Bill Payment Operation"
    MAKE_CASH_WITHDRAWAL_OPERATION = "Make Cash Withdrawal Operation"
    CREATE_USER = "Create User"
    GET_USER = "Get User"

class AllureFeature(StrEnum):
    ACCOUNTS_GATEWAY_SERVICE = "Accounts Gateway Service"
    CARDS_GATEWAY_SERVICE = "Cards Gateway Service"
    DOCUMENTS_GATEWAY_SERVICE = "Documents Gateway Service"
    OPERATIONS_GATEWAY_SERVICE = "Operations Gateway Service"
    USERS_GATEWAY_SERVICE = "Users Gateway Service"


class AllureEpic(StrEnum):
    GATEWAY_SERVICE = "Gateway Service"
