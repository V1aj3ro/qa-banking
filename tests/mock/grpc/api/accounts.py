from pathlib import Path

from grpc.aio import ServicerContext

from contracts.services.accounts.accounts_service_pb2_grpc import AccountsServiceServicer
from contracts.services.accounts.rpc_create_account_pb2 import CreateAccountRequest, CreateAccountResponse
from contracts.services.accounts.rpc_get_account_pb2 import GetAccountRequest, GetAccountResponse
from contracts.services.accounts.rpc_get_accounts_pb2 import GetAccountsRequest, GetAccountsResponse
from contracts.services.accounts.rpc_update_account_balance_pb2 import (
    UpdateAccountBalanceRequest,
    UpdateAccountBalanceResponse
)
from tests.mock.grpc.tools import get_scenario_grpc
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader

loader = MockLoader(
    root=Path("./tests/mock/grpc/data/accounts"),
    logger=get_test_logger("ACCOUNTS_SERVICE_MOCK_LOADER")
)

class AccountsMockService(AccountsServiceServicer):
    async def GetAccount(self, request: GetAccountRequest, context: ServicerContext) -> GetAccountResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f'GetAccount/{scenario}.json',
            model=GetAccountResponse
        )

    async def GetAccounts(self, request: GetAccountsRequest, context: ServicerContext) -> GetAccountsResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f'GetAccounts/{scenario}.json',
            model=GetAccountsResponse
        )

    async def CreateAccount(self, request: CreateAccountRequest, context: ServicerContext) -> CreateAccountResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f'CreateAccount/{scenario}.json',
            model=CreateAccountResponse
        )

    async def UpdateAccountBalance(
            self,
            request: UpdateAccountBalanceRequest,
            context: ServicerContext
    ) -> UpdateAccountBalanceResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f'UpdateAccountBalance/{scenario}.json',
            model=UpdateAccountBalanceResponse
        )
