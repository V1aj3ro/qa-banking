from pydantic import BaseModel, IPvAnyAddress


class GRPCClientTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress

    @property
    def url(self):
        return f"{self.address}:{self.port}"

class GRPCServerTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress

    @property
    def url(self):
        return f"{self.address}:{self.port}"