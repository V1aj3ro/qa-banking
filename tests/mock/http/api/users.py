import uuid
from pathlib import Path

from fastapi import APIRouter, Depends

from tests.context.scenario import Scenario
from tests.mock.http.tools import get_scenario_http
from tests.schema.users import GetUserResponseTestSchema, CreateUserResponseTestSchema, CreateUserRequestTestSchema
from tests.tools.logger import get_test_logger
from tests.tools.mock import MockLoader
from tests.tools.routes import APITestRoutes

loader = MockLoader(
    root=Path("./tests/mock/http/data/userss"),
    logger=get_test_logger("USERS_MOCK_SERVICE_LOADER")
)

users_mock_router = APIRouter(
    prefix=APITestRoutes.USERS,
    tags=[APITestRoutes.USERS]
)


@users_mock_router.get('/{user_id}', response_model=GetUserResponseTestSchema)
async def get_user_view(user_id: uuid.UUID, scenario: Scenario = Depends(get_scenario_http)):
    return await loader.load_http(
        file = f"get_user/{scenario}.json",
        model = GetUserResponseTestSchema
    )


@users_mock_router.post('', response_model=CreateUserResponseTestSchema)
async def create_user_view(request: CreateUserRequestTestSchema, scenario: Scenario = Depends(get_scenario_http)):
    return await loader.load_http(
        file = f"create_user/{scenario}.json",
        model = CreateUserResponseTestSchema
    )
