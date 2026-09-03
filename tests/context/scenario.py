from enum import StrEnum


class Scenario(StrEnum):
    USER_WITH_ONE_PURCHASE_AND_ONE_TOP_UP_OPERATIONS = "user_with_one_purchase_and_one_top_up_operations"
    USER_WITH_ACTIVE_DEBIT_CARD_ACCOUNT = "user_with_active_debit_card_account"