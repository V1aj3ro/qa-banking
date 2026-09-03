import uuid
from pathlib import Path

from fastapi import APIRouter, Depends

from tests.context.scenario import Scenario
from tests.mock.http.tools import get_scenario_http
from tests.schema.documents import (
    GetTariffResponseTestSchema,
    CreateTariffResponseTestSchema,
    CreateTariffRequestTestSchema
)
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader
from tests.tools.routes import APITestRoutes

loader = MockLoader(
    root=Path("./tests/mock/http/data/documents/tariffs"),
    logger=get_test_logger("TARIFFS_MOCK_SERVICE_LOADER")
)

tariffs_mock_router = APIRouter(
    prefix=APITestRoutes.TARIFFS,
    tags=[APITestRoutes.TARIFFS]
)

@tariffs_mock_router.get('/{account_id}', response_model=GetTariffResponseTestSchema)
async def get_tariff_view(account_id: uuid.UUID, scenario: Scenario = Depends(get_scenario_http)):
    return await loader.load_http(
        file = f"get_tariff/{scenario}.json", 
        model = GetTariffResponseTestSchema
    )


@tariffs_mock_router.post('', response_model=CreateTariffResponseTestSchema)
async def create_tariff_view(
        request: CreateTariffRequestTestSchema,
        scenario: Scenario = Depends(get_scenario_http)
):
    return await loader.load_http(
        file = f"create_tariff/{scenario}.json",
        model = CreateTariffResponseTestSchema
    )
