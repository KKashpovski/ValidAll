"""Функции с позитивным сценарием - тестируемые значения True."""
from typing import Any
import jsonschema
import re

json_schema = {
                "$schema": "http://json-schema.org/draft-07/schema",
                "$id": "http://example.com/example.json",
                "type": "object",
                "title": "The root schema",
                "description": "The root schema comprises the entire JSON document.",
                "default": {},
                "examples": [
                    {
                        "key": 123
                    }
                ],
                "required": [
                    "key"
                ],
                "properties": {
                    "key": {
                        "$id": "#/properties/key",
                        "type": "integer",
                        "title": "The key schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            123
                        ]
                    }
                }
            }


def validate_json(result: dict) -> bool:
    """input_validation."""
    try:
        jsonschema.validate(result, json_schema)
        return True
        # return not bool(jsonschema.validate(result, json_schema))
    except jsonschema.ValidationError:
        return False


def regex_func(argument: str) -> bool:
    """result_validation."""
    regex = re.compile("^[0-9]+$")
    return bool(regex.match(argument))


def default_func() -> Any:
    """Дефолтная функция."""
    abv = 'Что-то идет не так..., нужно перепроверить входные параметры.'
    return abv
