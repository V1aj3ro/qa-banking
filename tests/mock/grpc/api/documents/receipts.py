from pathlib import Path

from grpc.aio import ServicerContext

from contracts.services.documents.receipts.receipts_service_pb2_grpc import ReceiptsServiceServicer
from contracts.services.documents.receipts.rpc_create_receipt_pb2 import CreateReceiptRequest, CreateReceiptResponse
from contracts.services.documents.receipts.rpc_get_receipt_pb2 import GetReceiptRequest, GetReceiptResponse
from tests.mock.grpc.tools import get_scenario_grpc
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader

loader = MockLoader(
    root=Path("./tests/mock/grpc/data/documents/receipts"),
    logger=get_test_logger("DOCUMENTS_RECEIPTS_SERVICE_MOCK_LOADER")
)

class ReceiptsMockService(ReceiptsServiceServicer):
    async def GetReceipt(self, request: GetReceiptRequest, context: ServicerContext) -> GetReceiptResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f"GetReceipt/{scenario}.json",
            model=GetReceiptResponse
        )

    async def CreateReceipt(self, request: CreateReceiptRequest, context: ServicerContext) -> CreateReceiptResponse:
        scenario = await get_scenario_grpc(context)
        return await loader.load_grpc(
            file=f"CreateReceipt/{scenario}.json",
            model=CreateReceiptResponse
        )
