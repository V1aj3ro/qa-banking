from datetime import date, datetime
from typing import Self

from fastapi import Query
from pydantic import BaseModel, Field, ConfigDict, UUID4
from pydantic.alias_generators import to_camel

from libs.schema.query import QuerySchema
from tests.tools.fakers import fake
from tests.types.operations import OperationTestType, OperationTestStatus


class OperationTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )
    id: str
    type: OperationTestType
    status: OperationTestStatus
    amount: float
    card_id: str
    category: str
    created_at: str
    account_id: str


class OperationReceiptTestSchema(BaseModel):
    url: str
    document: str


class OperationsSummaryTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )
    spent_amount: float
    received_amount: float
    cashback_amount: float


class GetOperationResponseTestSchema(BaseModel):
    operation: OperationTestSchema


class GetOperationsQueryTestSchema(QuerySchema):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )
    account_id: str

    @classmethod
    async def as_query(cls, account_id: str = Query(alias="accountId")) -> Self:
        return GetOperationsSummaryQueryTestSchema(account_id=account_id)

class GetOperationsResponseTestSchema(BaseModel):
    operations: list[OperationTestSchema]


class GetOperationsSummaryQueryTestSchema(QuerySchema):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    account_id: str

    @classmethod
    async def as_query(cls, account_id: str = Query(alias="accountId")) -> Self:
        return GetOperationsSummaryQueryTestSchema(account_id=account_id)


class GetOperationsSummaryResponseTestSchema(BaseModel):
    summary: OperationsSummaryTestSchema


class GetOperationReceiptResponseTestSchema(BaseModel):
    receipt: OperationReceiptTestSchema


class MakeOperationRequestTestSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        validate_by_alias=True,
        validate_by_name=True
    )

    status: OperationTestStatus = Field(default_factory=lambda: fake.enum(OperationTestStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str
    account_id: str


class MakeFeeOperationRequestTestSchema(MakeOperationRequestTestSchema):
    pass


class MakeFeeOperationResponseTestSchema(BaseModel):
    operation: OperationTestSchema


class MakeTopUpOperationRequestTestSchema(MakeOperationRequestTestSchema):
    pass


class MakeTopUpOperationResponseTestSchema(BaseModel):
    operation: OperationTestSchema


class MakeCashbackOperationRequestTestSchema(MakeOperationRequestTestSchema):
    pass


class MakeCashbackOperationResponseTestSchema(BaseModel):
    operation: OperationTestSchema


class MakeTransferOperationRequestTestSchema(MakeOperationRequestTestSchema):
    pass


class MakeTransferOperationResponseTestSchema(BaseModel):
    operation: OperationTestSchema


class MakePurchaseOperationRequestTestSchema(MakeOperationRequestTestSchema):
    category: str = Field(default_factory=fake.category)


class MakePurchaseOperationResponseTestSchema(BaseModel):
    operation: OperationTestSchema


class MakeBillPaymentOperationRequestTestSchema(MakeOperationRequestTestSchema):
    pass


class MakeBillPaymentOperationResponseTestSchema(BaseModel):
    operation: OperationTestSchema


class MakeCashWithdrawalOperationRequestTestSchema(MakeOperationRequestTestSchema):
    pass


class MakeCashWithdrawalOperationResponseTestSchema(BaseModel):
    operation: OperationTestSchema



# Schemas for mocks



class CreateOperationRequestTestSchema(BaseModel):
    type: OperationTestType
    status: OperationTestStatus
    amount: float
    card_id: UUID4
    category: str
    created_at: datetime
    account_id: UUID4


class CreateOperationResponseTestSchema(BaseModel):
    operation: OperationTestSchema



class GetOperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummaryTestSchema
