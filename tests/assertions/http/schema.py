from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator

from tests.tools.logger import get_test_logger

logger = get_test_logger("SCHEMA_ASSERTIONS")


@allure.step("Validation JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:
    logger.info("Validating JSON schema")

    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )
