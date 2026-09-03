import uuid
from pathlib import Path

from fastapi import APIRouter, Depends

from tests.context.scenario import Scenario
from tests.mock.http.tools import get_scenario_http
from tests.schema.documents import GetContractResponseTestSchema, CreateContractResponseTestSchema, \
    CreateContractRequestTestSchema
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader
from tests.tools.routes import APITestRoutes

loader = MockLoader(
    root=Path("./tests/mock/http/data/documents/contracts"),
    logger=get_test_logger("CONTRACTS_MOCK_SERVICE_LOADER")
)

contracts_mock_router = APIRouter(
    prefix=APITestRoutes.CONTRACTS,
    tags=[APITestRoutes.CONTRACTS]
)

@contracts_mock_router.get('/{account_id}', response_model=GetContractResponseTestSchema)
async def get_contract_view(account_id: uuid.UUID, scenario: Scenario = Depends(get_scenario_http)):
    return await loader.load_http(
        file = f"get_contract/{scenario}.json",
        model = GetContractResponseTestSchema
    )


@contracts_mock_router.post('', response_model=CreateContractResponseTestSchema)
async def create_contract_view(
        request: CreateContractRequestTestSchema,
        scenario: Scenario = Depends(get_scenario_http)
):
    return await loader.load_http(
        file = f"create_contract/{scenario}.json",
        model = CreateContractResponseTestSchema
    )
