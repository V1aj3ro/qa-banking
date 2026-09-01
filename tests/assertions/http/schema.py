from typing import Any

import allure
from jsonschema import validate
from jsonschema.validators import Draft202012Validator


@allure.step("Validation JSON schema")
def validate_json_schema(instance: Any, schema: dict) -> None:

    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )
