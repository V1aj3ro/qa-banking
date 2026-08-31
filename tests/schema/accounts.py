from pydantic import BaseModel, ConfigDict, UUID4
from pydantic.alias_generators import to_camel

from tests.schema.cards import CardTestSchema
from tests.types.accounts import AccountTestType, AccountTestStatus


class AccountTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    id: UUID4
    type: AccountTestType
    cards: list[CardTestSchema]
    status: AccountTestStatus
    user_id: UUID4
    balance: float


class GetAccountsQueryTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id: UUID4


class GetAccountsResponseTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    accounts: list[AccountTestSchema]


class OpenDepositAccountRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id: UUID4


class OpenDepositAccountResponseTestSchema(BaseModel):
    account: AccountTestSchema


class OpenSavingsAccountRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id: UUID4


class OpenSavingsAccountResponseTestSchema(BaseModel):
    account: AccountTestSchema


class OpenDebitCardAccountRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id: UUID4

class OpenDebitCardAccountResponseTestSchema(BaseModel):
    account: AccountTestSchema


class OpenCreditCardAccountRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id: UUID4


class OpenCreditCardAccountResponseSchema(BaseModel):
    account: AccountTestSchema