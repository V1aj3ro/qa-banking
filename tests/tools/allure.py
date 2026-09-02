from enum import StrEnum


class AllureTag(StrEnum):
    GRPC = "GRPC"
    HTTP = "HTTP"
    KAFKA = "KAFKA"
    POSTGRES = "POSTGRES"

    GATEWAY_SERVICE = "GATEWAY_SERVICE"


class AllureStory(StrEnum):
    OPEN_DEBIT_CARD_ACCOUNT = "Open Debit Card Account"
    ISSUE_VIRTUAL_CARD = "Issue Virtual Card"
    GET_TARIFF_DOCUMENT = "Get Tariff Document"
    MAKE_FEE_OPERATION = "Make Fee Operation"
    CREATE_USER = "Create User"

class AllureFeature(StrEnum):
    ACCOUNTS_GATEWAY_SERVICE = "Accounts Gateway Service"
    CARDS_GATEWAY_SERVICE = "Cards Gateway Service"
    DOCUMENTS_GATEWAY_SERVICE = "Documents Gateway Service"
    OPERATIONS_GATEWAY_SERVICE = "Operations Gateway Service"
    USERS_GATEWAY_SERVICE = "Users Gateway Service"


class AllureEpic(StrEnum):
    GATEWAY_SERVICE = "Gateway Service"
