import uuid
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends

from tests.context.scenario import Scenario
from tests.mock.http.tools import get_scenario_http
from tests.schema.operations import (
    GetOperationsResponseTestSchema,
    GetOperationsQueryTestSchema,
    GetOperationsSummaryResponseTestSchema,
    GetOperationsSummaryQueryTestSchema,
    GetOperationResponseTestSchema,
    CreateOperationResponseTestSchema,
    CreateOperationRequestTestSchema
)
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader
from tests.tools.routes import APITestRoutes

loader = MockLoader(
    root=Path("./tests/mock/http/data/operations"),
    logger=get_test_logger("OPERATIONS_MOCK_SERVICE_LOADER")
)

operations_mock_router = APIRouter(
    prefix=APITestRoutes.OPERATIONS,
    tags=[APITestRoutes.OPERATIONS]
)


@operations_mock_router.get('', response_model=GetOperationsResponseTestSchema)
async def get_operations_view(
        query: Annotated[GetOperationsQueryTestSchema,
        Depends(GetOperationsQueryTestSchema.as_query)],
        scenario: Scenario = Depends(get_scenario_http)
):
    return await loader.load_http(
        file = f"get_operations/{scenario}.json",
        model = GetOperationsResponseTestSchema
    )


@operations_mock_router.get(
    '/operations-summary',
    response_model=GetOperationsSummaryResponseTestSchema
)
async def get_operations_summary_view(
        query: Annotated[GetOperationsSummaryQueryTestSchema,
        Depends(GetOperationsSummaryQueryTestSchema.as_query)],
        scenario: Scenario = Depends(get_scenario_http)
):
    return await loader.load_http(
        file = f"get_operations_summary/{scenario}.json",
        model = GetOperationsSummaryResponseTestSchema
    )


@operations_mock_router.get('/{operation_id}', response_model=GetOperationResponseTestSchema)
async def get_operation_view(operation_id: uuid.UUID, scenario: Scenario = Depends(get_scenario_http)):
    return await loader.load_http(
        file = f"get_operation/{scenario}.json",
        model = GetOperationResponseTestSchema
    )



@operations_mock_router.post('', response_model=CreateOperationResponseTestSchema)
async def create_operation_view(
        request: CreateOperationRequestTestSchema,
        scenario: Scenario = Depends(get_scenario_http)
):
    return await loader.load_http(
        file=f"create_operation/{scenario}.json",
        model=CreateOperationResponseTestSchema
    )
