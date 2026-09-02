from pydantic import BaseModel

from tests.schema.cards import IssueVirtualCardRequestTestSchema, IssueVirtualCardResponseTestSchema


class VirtualCardHTTPFixture(BaseModel):
    request: IssueVirtualCardRequestTestSchema
    response: IssueVirtualCardResponseTestSchema

    @property
    def id(self) -> str:
        return self.response.card.id

