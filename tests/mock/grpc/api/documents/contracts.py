from pathlib import Path

from grpc.aio import ServicerContext

from contracts.services.documents.contracts.contracts_service_pb2_grpc import ContractsServiceServicer
from contracts.services.documents.contracts.rpc_create_contract_pb2 import CreateContractRequest, CreateContractResponse
from contracts.services.documents.contracts.rpc_get_contract_pb2 import GetContractRequest, GetContractResponse
from tests.mock.grpc.tools import get_scenario_grpc
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader

loader = MockLoader(
    root=Path("./tests/mock/grpc/data/documents/contracts"),
    logger=get_test_logger("DOCUMENTS_CONTRACTS_SERVICE_MOCK_LOADER")
)

class ContractsMockService(ContractsServiceServicer):
    async def GetContract(self, request: GetContractRequest, context: ServicerContext) -> GetContractResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f"GetContract/{scenario}.json",
            model=GetContractResponse
        )

    async def CreateContract(self, request: CreateContractRequest, context: ServicerContext) -> CreateContractResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f"CreateContract/{scenario}.json",
            model=CreateContractResponse
        )
