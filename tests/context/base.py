from typing import Optional

from pydantic import BaseModel

from tests.context.scenario import Scenario


class RequestContext(BaseModel):
    scenario: Scenario


def build_grpc_test_metadata(context: Optional[RequestContext] | None) -> list[tuple[str, str]] | None:
    if context is None:
        return None
    scenario_value = context.scenario.value if hasattr(context.scenario, 'value') else str(context.scenario)
    return [("x-test-scenario", scenario_value)]


def build_http_test_headers(context: Optional[RequestContext] | None) -> dict[str, str] | None:
    if context is None:
        return None
    return {"x-test-scenario": context.scenario}
