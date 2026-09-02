from logging import Logger

import grpc
from tests.clients.grpc.interceptors.logger_interceptor import GRPCLoggerInterceptor
from tests.config import test_settings

def build_gateway_grpc_test_client(logger: Logger) -> grpc.Channel:
    channel = grpc.insecure_channel(test_settings.gateway_grpc_client.client_url)

    return grpc.intercept_channel(channel, GRPCLoggerInterceptor(logger=logger))