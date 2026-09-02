from pydantic import BaseModel

from tests.schema.operations import MakeFeeOperationRequestTestSchema, MakeFeeOperationResponseTestSchema


class FeeOperationHTTPFixture(BaseModel):
    request: MakeFeeOperationRequestTestSchema
    response: MakeFeeOperationResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.operation.id

