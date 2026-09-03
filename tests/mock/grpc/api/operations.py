from pathlib import Path

from grpc.aio import ServicerContext

from contracts.services.operations.operations_service_pb2_grpc import OperationsServiceServicer
from contracts.services.operations.rpc_create_operation_pb2 import CreateOperationRequest, CreateOperationResponse
from contracts.services.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse
)
from tests.mock.grpc.tools import get_scenario_grpc
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader



loader = MockLoader(
    root=Path("./tests/mock/grpc/data/operations"),
    logger=get_test_logger("OPERATIONS_SERVICE_MOCK_LOADER")
)


class OperationsMockService(OperationsServiceServicer):
    async def GetOperation(self, request: GetOperationRequest, context: ServicerContext) -> GetOperationResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f"GetOperation/{scenario}.json",
            model=GetOperationResponse
        )

    async def GetOperations(self, request: GetOperationsRequest, context: ServicerContext) -> GetOperationsResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f"GetOperations/{scenario}.json",
            model=GetOperationsResponse
        )

    async def CreateOperation(
            self,
            request: CreateOperationRequest,
            context: ServicerContext
    ) -> CreateOperationResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f"CreateOperation/{scenario}.json",
            model=CreateOperationResponse
        )

    async def GetOperationsSummary(
            self,
            request: GetOperationsSummaryRequest,
            context: ServicerContext
    ) -> GetOperationsSummaryResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f"GetOperationsSummary/{scenario}.json",
            model=GetOperationsSummaryResponse
        )
