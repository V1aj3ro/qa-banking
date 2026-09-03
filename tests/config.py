from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from tests.tools.config.grpc import GRPCClientTestConfig, GRPCServerTestConfig
from tests.tools.config.http import HTTPClientTestConfig, HTTPServerTestConfig


class TestSettings(BaseSettings):

    model_config = SettingsConfigDict(
        extra="allow",
        env_file=Path(__file__).parent / ".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    mock_http_server: HTTPServerTestConfig
    mock_grpc_server: GRPCServerTestConfig

    gateway_http_client: HTTPClientTestConfig
    gateway_grpc_client: GRPCClientTestConfig




test_settings = TestSettings()
