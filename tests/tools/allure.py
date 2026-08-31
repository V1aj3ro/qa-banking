from enum import StrEnum


class AllureTag(StrEnum):
    GRPC = "GRPC"
    HTTP = "HTTP"
    KAFKA = "KAFKA"
    POSTGRES = "POSTGRES"

    GATEWAY_SERVICE = "GATEWAY_SERVICE"


class AllureStory(StrEnum):
    ...

class AllureFeature(StrEnum):
    GATEWAY_SERVICE = "Gateway Service"
