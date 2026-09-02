from pydantic import BaseModel, ConfigDict

from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import (
    IssueVirtualCardRequest,
    IssueVirtualCardResponse
)


class VirtualCardGRPCFixture(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    request: IssueVirtualCardRequest
    response: IssueVirtualCardResponse

    @property
    def id(self) -> str:
        return self.response.card.id

