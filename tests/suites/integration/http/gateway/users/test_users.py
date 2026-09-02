from http import HTTPStatus

import allure
import pytest

from tests.assertions.base import assert_status_code
from tests.assertions.http.schema import validate_json_schema
from tests.assertions.http.users import assert_create_user_response
from tests.clients.http.gateway.users.client import UsersGatewayHTTPTestClient
from tests.schema.users import CreateUserRequestTestSchema, CreateUserResponseTestSchema
from tests.tools.allure import AllureTag, AllureStory, AllureFeature, AllureEpic


@pytest.mark.gateway
@pytest.mark.gateway_users
@pytest.mark.regression
@allure.tag(AllureTag.HTTP, AllureTag.GATEWAY_SERVICE)
@allure.epic(AllureEpic.GATEWAY_SERVICE)
@allure.feature(AllureFeature.USERS_GATEWAY_SERVICE)
class TestUsersHTTP:
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