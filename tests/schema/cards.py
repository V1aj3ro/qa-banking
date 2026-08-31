from datetime import date

from pydantic import BaseModel, UUID4, ConfigDict
from pydantic.alias_generators import to_camel

from tests.types.cards import CardTestType, CardTestStatus, CardTestPaymentSystem


class CardTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )
    id: UUID4
    pin: str
    cvv: str
    type: CardTestType
    status: CardTestStatus
    account_id: UUID4
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

    user_id: UUID4
    account_id: UUID4


class IssueVirtualCardResponseTestSchema(BaseModel):
    card: CardTestSchema


class IssuePhysicalCardRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    user_id:UUID4
    account_id: UUID4


class IssuePhysicalCardResponseTestSchema(BaseModel):
    card: CardTestSchema
