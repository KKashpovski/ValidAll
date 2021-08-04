"""Тестирование валидатора."""
import json
import unittest
from typing import Any
import main
from main import valid_all
from main import InputParameterVerificationError
from main import ResultVerificationError
from my_func import validate_json
from my_func import regex_func
from my_func import default_func


class MyTestClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for test"""
        print("Tear down for [" + self.shortDescription() + "]")
        print("")

    def test_positive_validate_json(self):
        """Валидация входного json-параметра с ожидаемым положительным исходом."""
        @valid_all(input_validation=validate_json,
                   result_validation=regex_func,
                   on_fail_repeat_times=1,
                   default_behavior=default_func)
        def my_func(argument: str) -> dict:
            """Функция, принимаемое и возвращаемое значение которой нужно провалидировать."""
            x = '{"key": 123}'
            y = json.loads(x)
            return y

        test = my_func('{"key": 123}')
        self.assertTrue(test)

    def test_validate_string(self):
        """Валидация строки по регулярному выражению."""
        pass

    def test_validate_result(self):
        """Проверка валидации возвращаемого результата."""
        @valid_all(input_validation=validate_json,
                   result_validation=regex_func,
                   on_fail_repeat_times=1,
                   default_behavior=default_func)
        def my_func(argument: dict) -> str:
            """Функция, принимаемое и возвращаемое значение которой нужно провалидировать."""
            x = '{"key": 123}'
            return x

        try:
            res = my_func({"key": 123})
        except ResultVerificationError as err:
            return err
        assert type(res) == str

    # def test_input_error(self):
    #     """Проверка поднятия исключения InputParameterVerificationError."""
    #
    #     @valid_all(input_validation=validate_json,
    #                result_validation=regex_func,
    #                on_fail_repeat_times=1,
    #                default_behavior=default_func)
    #     def my_func(*args: Any, **kwargs: Any) -> Any:
    #         """Функция, принимаемое и возвращаемое значение которой нужно провалидировать."""
    #         return {'key': '123'}
    #
    #     try:
    #         res = my_func(123)
    #     except InputParameterVerificationError as err:
    #         res = err
    #     self.assert type(res)
    #     self.assertRaises(InputParameterVerificationError)
    #
    # def test_result_error(self, on_fail_repeat_times=0):
    #     """Проверка поднятия исключения ResultVerificationError."""
    #     @valid_all(input_validation=validate_json,
    #                result_validation=regex_func,
    #                on_fail_repeat_times=1,
    #                default_behavior=default_func)
    #     def my_func(argument: dict) -> str:
    #         """Функция, принимаемое и возвращаемое значение которой нужно провалидировать."""
    #         return json["key"]
    #
    #     # try:
    #     #     result = my_func(result_error)
    #     # except ResultVerificationError as ex:
    #     #     result = ex
    #     self.assertRaises(ResultVerificationError)
    #

if __name__ == "__main__":
    unittest.main()
