"""Тестирование валидатора."""
import unittest
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

    def test_validate_json(self):
        """Валидация входного json-параметра с ожидаемым положительным исходом."""
        @valid_all(input_validation=validate_json,
                   result_validation=regex_func,
                   on_fail_repeat_times=1,
                   default_behavior=None)
        def my_func(argument: str) -> dict:
            """Функция, принимаемое и возвращаемое значение которой нужно провалидировать."""
            return {"key": int(argument)}

        try:
            my_func('123')
            test = True
            return test
        except InputParameterVerificationError:
            test = False
            return test
        self.assertTrue(test)

    def test_validate_string(self):
        """Валидация строки по регулярному выражению."""
        pass

    def test_validate_result(self):
        """Проверка валидации возвращаемого результата."""
        pass

    def test_input_error(self):
        """Проверка поднятия исключения InputParameterVerificationError."""

        @valid_all(input_validation=validate_json,
                   result_validation=regex_func,
                   on_fail_repeat_times=1,
                   default_behavior=default_func)
        def my_func(argument: str) -> dict:
            """Функция, принимаемое и возвращаемое значение которой нужно провалидировать."""
            return {"key": int(argument)}

        try:
            result = my_func('{"key": 123}')
        except InputParameterVerificationError as err:
            result = err
        assert type(result) == InputParameterVerificationError
        self.assertRaises(InputParameterVerificationError)

    def test_result_error(self, on_fail_repeat_times=0):
        """Проверка поднятия исключения ResultVerificationError."""
        pass


if __name__ == "__main__":
    unittest.main()
