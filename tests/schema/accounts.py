from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from tests.schema.cards import CardTestSchema
from tests.types.accounts import AccountTestType, AccountTestStatus


class AccountTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    id: str
    type: AccountTestType
    cards: list[CardTestSchema]
    status: AccountTestStatus
    balance: float


class GetAccountsQueryTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id: str

class GetAccountResponseTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    account: AccountTestSchema


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

    user_id: str


class OpenDepositAccountResponseTestSchema(BaseModel):
    account: AccountTestSchema


class OpenSavingsAccountRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id: str


class OpenSavingsAccountResponseTestSchema(BaseModel):
    account: AccountTestSchema


class OpenDebitCardAccountRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id: str

class OpenDebitCardAccountResponseTestSchema(BaseModel):
    account: AccountTestSchema


class OpenCreditCardAccountRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id: str


class OpenCreditCardAccountResponseTestSchema(BaseModel):
    account: AccountTestSchema


# Schemas for mocks

class CreateAccountRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )


    type: AccountTestType
    status: AccountTestStatus
    user_id: str
    balance: float

class CreateAccountResponseTestSchema(BaseModel):
    account: AccountTestSchema

class UpdateAccountBalanceRequestTestSchema(BaseModel):
    balance: float
    account_id: str


class UpdateAccountBalanceResponseTestSchema(BaseModel):
    account: AccountTestSchema

