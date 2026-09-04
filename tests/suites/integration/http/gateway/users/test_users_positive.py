from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.schema import validate_json_schema
from tests.assertions.http.users import (
    assert_create_user_response,
    assert_get_user_response,
    assert_get_user_response_with_incorrect_user_id
)
from tests.clients.http.gateway.users.client import UsersGatewayHTTPTestClient
from tests.fixtures.http.gateway.users.schema import UserHTTPFixture
from tests.schema.errors import ValidationErrorResponseSchema
from tests.schema.users import CreateUserRequestTestSchema, CreateUserResponseTestSchema, GetUserResponseTestSchema
from tests.tools.allure import AllureTag, AllureStory, AllureFeature, AllureEpic


@pytest.mark.gateway
@pytest.mark.gateway_users
@pytest.mark.regression
@pytest.mark.positive
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE, AllureTag.POSITIVE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.USERS_GATEWAY_SERVICE)
class TestUsersPositiveHTTP:
    @allure.story(AllureStory.CREATE_USER)
    @allure.title("[HTTP] Create user")
    def test_create_user(
            self,
            users_gateway_http_test_client: UsersGatewayHTTPTestClient
    ):
        request = CreateUserRequestTestSchema()
        response = users_gateway_http_test_client.create_user_api(request)
        response_data = CreateUserResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_USER)
    @allure.title("[HTTP] Get user")
    def test_get_user(self, function_http_user: UserHTTPFixture, users_gateway_http_test_client: UsersGatewayHTTPTestClient):
        response = users_gateway_http_test_client.get_user_api(function_http_user.id)
        response_data = GetUserResponseTestSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(response_data, function_http_user.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.story(AllureStory.GET_USER)
    @allure.title("[HTTP] Get user with incorrect user id")
    def test_get_user_with_incorrect_user_id(self, users_gateway_http_test_client: UsersGatewayHTTPTestClient):
        response = users_gateway_http_test_client.get_user_api(user_id="incorrect-user-id")
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_get_user_response_with_incorrect_user_id(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
