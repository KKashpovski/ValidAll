"""Функции с позитивным сценарием - тестируемые значения True."""
from typing import Any

import jsonschema
import re

# json_data = {
#                 "key": 123
#             }
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


def validate_json():
    """."""
    json_data = '123'
    # try:
    #     return not bool(jsonschema.validate(json_data, json_schema))
    # except jsonschema.ValidationError:
    #     return False
    try:
        jsonschema.validate(json_data, json_schema)
        pre_condition = True
        return pre_condition
    except jsonschema.exceptions.ValidationError:
        pre_condition = False
        return pre_condition


def regex_func(argument: str) -> bool:
    """."""
    regex = re.compile("^[0-9]+$")
    return bool(regex.match(argument))


def default_func(*args: Any, **kwargs: Any) -> Any:
    """Дефолтная функция."""
    abv = 'Что-то идет не так..., нужно перепроверить входные параметры.'
    return abv

