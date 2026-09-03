from pydantic import BaseModel, HttpUrl


class DocumentTestSchema(BaseModel):
    url: HttpUrl
    document: str

class ContractTestSchema(BaseModel):
    url: HttpUrl
    document: bytes

class ReceiptTestSchema(BaseModel):
    url: HttpUrl
    document: bytes


class TariffTestSchema(BaseModel):
    url: HttpUrl
    document: bytes


class GetReceiptResponseTestSchema(BaseModel):
    receipt: ReceiptTestSchema


class GetTariffDocumentResponseTestSchema(BaseModel):
    tariff: TariffTestSchema


class GetContractDocumentResponseTestSchema(BaseModel):
    contract: ContractTestSchema


# Schemas for mocks


class GetContractResponseTestSchema(BaseModel):
    contract: ContractTestSchema


class CreateContractRequestTestSchema(BaseModel):
    content: bytes
    account_id: str


class CreateContractResponseTestSchema(BaseModel):
    contract: ContractTestSchema




class CreateReceiptRequestTestSchema(BaseModel):
    content: bytes
    operation_id: str


class CreateReceiptResponseTestSchema(BaseModel):
    receipt: ReceiptTestSchema



class GetTariffResponseTestSchema(BaseModel):
    tariff: TariffTestSchema


class CreateTariffRequestTestSchema(BaseModel):
    content: bytes
    account_id: str


class CreateTariffResponseTestSchema(BaseModel):
    tariff: TariffTestSchema
