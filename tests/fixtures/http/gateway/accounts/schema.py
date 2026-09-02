from pydantic import BaseModel

from tests.schema.accounts import (
    OpenDebitCardAccountRequestTestSchema,
    OpenDebitCardAccountResponseTestSchema,
    OpenCreditCardAccountRequestTestSchema,
    OpenCreditCardAccountResponseTestSchema,
    OpenDepositAccountRequestTestSchema,
    OpenDepositAccountResponseTestSchema,
    OpenSavingsAccountRequestTestSchema,
    OpenSavingsAccountResponseTestSchema
)


class DebitCardAccountHTTPFixture(BaseModel):
    request: OpenDebitCardAccountRequestTestSchema
    response: OpenDebitCardAccountResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.account.id


class CreditCardAccountHTTPFixture(BaseModel):
    request: OpenCreditCardAccountRequestTestSchema
    response: OpenCreditCardAccountResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.account.id


class DepositAccountHTTPFixture(BaseModel):
    request: OpenDepositAccountRequestTestSchema
    response: OpenDepositAccountResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.account.id


class SavingsAccountHTTPFixture(BaseModel):
    request: OpenSavingsAccountRequestTestSchema
    response: OpenSavingsAccountResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.account.id


