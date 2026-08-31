from pydantic import BaseModel, HttpUrl


class DocumentTestSchema(BaseModel):
    url: HttpUrl
    document: str


class GetTariffDocumentResponseTestSchema(BaseModel):
    tariff: DocumentTestSchema


class GetContractDocumentResponseTestSchema(BaseModel):
    contract: DocumentTestSchema
