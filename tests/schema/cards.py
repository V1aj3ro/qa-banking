from datetime import date
from typing import Self

from fastapi import Query
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

from libs.schema.query import QuerySchema
from tests.types.cards import CardTestType, CardTestStatus, CardTestPaymentSystem


class CardTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )
    id: str
    pin: str
    cvv: str
    type: CardTestType
    status: CardTestStatus
    account_id: str
    card_number: str
    card_holder: str
    expiry_date: date
    payment_system: CardTestPaymentSystem


class IssueVirtualCardRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id: str
    account_id: str


class IssueVirtualCardResponseTestSchema(BaseModel):
    card: CardTestSchema


class IssuePhysicalCardRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id:str
    account_id: str


class IssuePhysicalCardResponseTestSchema(BaseModel):
    card: CardTestSchema


# Schemas for mocks


class GetCardsResponseTestSchema(BaseModel):
    cards: list[CardTestSchema]


class GetCardsQueryTestSchema(QuerySchema):
    account_id: str

    @classmethod
    async def as_query(cls, account_id: str = Query(alias="accountId")) -> Self:
        return GetCardsQueryTestSchema(account_id=account_id)


class GetCardResponseTestSchema(BaseModel):
    card: CardTestSchema


class CreateCardRequestTestSchema(BaseModel):
    pin: str
    cvv: str
    type: CardTestType
    status: CardTestStatus
    account_id: str
    card_number: str
    card_holder: str
    expiry_date: date
    payment_system: CardTestPaymentSystem

class CreateCardResponseTestSchema(BaseModel):
    card: CardTestSchema