from pydantic import BaseModel, ConfigDict

from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse
)


class FeeOperationGRPCFixture(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: MakeFeeOperationRequest
    response: MakeFeeOperationResponse

    @property
    def id(self) -> str:
        return self.response.operation.id

