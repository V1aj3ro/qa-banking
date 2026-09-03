from pathlib import Path

from grpc.aio import ServicerContext

from contracts.services.documents.tariffs.tariffs_service_pb2_grpc import TariffsServiceServicer
from contracts.services.documents.tariffs.rpc_create_tariff_pb2 import CreateTariffRequest, CreateTariffResponse
from contracts.services.documents.tariffs.rpc_get_tariff_pb2 import GetTariffRequest, GetTariffResponse
from tests.mock.grpc.tools import get_scenario_grpc
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader

loader = MockLoader(
    root=Path("./tests/mock/grpc/data/documents/tariffs"),
    logger=get_test_logger("DOCUMENTS_TARIFFS_SERVICE_MOCK_LOADER")
)

class TariffsMockService(TariffsServiceServicer):
    async def GetTariff(self, request: GetTariffRequest, context: ServicerContext) -> GetTariffResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f"GetTariff/{scenario}.json",
            model=GetTariffResponse
        )

    async def CreateTariff(self, request: CreateTariffRequest, context: ServicerContext) -> CreateTariffResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f"CreateTariff/{scenario}.json",
            model=CreateTariffResponse
        )
