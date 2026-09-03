import uuid
from pathlib import Path

from fastapi import APIRouter, Depends

from tests.context.scenario import Scenario
from tests.mock.http.tools import get_scenario_http
from tests.schema.documents import (
    GetReceiptResponseTestSchema,
    CreateReceiptResponseTestSchema,
    CreateReceiptRequestTestSchema
)
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader
from tests.tools.routes import APITestRoutes

loader = MockLoader(
    root=Path("./tests/mock/http/data/documents/receipts"),
    logger=get_test_logger("RECEIPTS_MOCK_SERVICE_LOADER")
)

receipts_mock_router = APIRouter(
    prefix=APITestRoutes.RECEIPTS,
    tags=[APITestRoutes.RECEIPTS]
)

@receipts_mock_router.get('/{account_id}', response_model=GetReceiptResponseTestSchema)
async def get_contract_view(account_id: uuid.UUID, scenario: Scenario = Depends(get_scenario_http)):
    return await loader.load_http(
        file = f"get_contract/{scenario}.json", 
        model = GetReceiptResponseTestSchema
    )


@receipts_mock_router.post('', response_model=CreateReceiptResponseTestSchema)
async def create_contract_view(
        request: CreateReceiptRequestTestSchema,
        scenario: Scenario = Depends(get_scenario_http)
):
    return await loader.load_http(
        file = f"create_contract/{scenario}.json",
        model = CreateReceiptResponseTestSchema
    )
