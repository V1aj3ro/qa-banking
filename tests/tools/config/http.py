from pydantic import BaseModel, HttpUrl, IPvAnyAddress


class HTTPClientTestConfig(BaseModel):
    url: HttpUrl
    timeout: float = 120.0



class HTTPServerTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress
