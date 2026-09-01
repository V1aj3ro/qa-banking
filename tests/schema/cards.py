from datetime import date

from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

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
