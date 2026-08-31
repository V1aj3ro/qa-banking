from pydantic import BaseModel, HttpUrl, IPvAnyAddress


class HTTPClientTestConfig(BaseModel):
    url: HttpUrl
    timeout: float = 120.0

    @property
    def client_url(self) -> str:
        return str(self.url)


class HTTPServerTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress
