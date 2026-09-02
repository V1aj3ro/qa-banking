from pydantic import BaseModel, ConfigDict

from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountRequest,
    OpenCreditCardAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import (
    OpenDepositAccountRequest,
    OpenDepositAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import (
    OpenSavingsAccountRequest,
    OpenSavingsAccountResponse
)


class DebitCardAccountGRPCFixture(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: OpenDebitCardAccountRequest
    response: OpenDebitCardAccountResponse

    @property
    def id(self) -> str:
        return self.response.account.id


class CreditCardAccountGRPCFixture(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: OpenCreditCardAccountRequest
    response: OpenCreditCardAccountResponse

    @property
    def id(self) -> str:
        return self.response.account.id


class DepositAccountGRPCFixture(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: OpenDepositAccountRequest
    response: OpenDepositAccountResponse

    @property
    def id(self) -> str:
        return self.response.account.id


class SavingsAccountGRPCFixture(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: OpenSavingsAccountRequest
    response: OpenSavingsAccountResponse

    @property
    def id(self) -> str:
        return self.response.account.id


