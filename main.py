"""ValidAll - универсальный декоратор для валидации входных и выходных параметров функции."""

from typing import Callable, Any


def valid_all(input_validation: Callable, result_validation: Callable, on_fail_repeat_times: int,
              default_behavior: Callable) -> Callable:
    """Декоратор."""
    def my_decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if input_validation(*args, **kwargs):
                print("Исходные параметры прошли проверку.")
                result = func(*args, **kwargs)
                if result_validation(result):
                    print("Результат функции прошел проверку.")
                    return result
                else:
                    if default_behavior(*args, **kwargs) is None:
                        raise ResultVerificationError("exception occur", ["Попробуй другие данные."])
                    else:
                        for i in range(0, abs(on_fail_repeat_times) + 1):
                            while True:
                                if on_fail_repeat_times == 0:
                                    raise ZeroValueError("exception occur", ["Попробуй другие данные."])
                                elif on_fail_repeat_times > 0:
                                    func(*args, **kwargs)
                                elif on_fail_repeat_times < 0:
                                    func(*args, **kwargs)
                                    continue
                        default_behavior(*args, **kwargs)
            else:
                raise InputParameterVerificationError("exception occur", ["Попробуй другие данные."])
        return wrapper
    return my_decorator


class InputParameterVerificationError(Exception):
    """."""

    def __init__(self, message: Any, errors_list: Any):
        """."""
        # Сначала вызов конструктора базового класса с параметрами которые ему нужны
        super().__init__(message)
        # Затем свой код исключения
        self.errors_list = errors_list

    def __str__(self) -> Any:
        """."""
        return "Входные параметры не подходят: " + str(self.errors_list)


class ResultVerificationError(Exception):
    """."""

    def __init__(self, message: Any, errors_list: Any):
        """."""
        # Сначала вызов конструктора базового класса с параметрами которые ему нужны
        super().__init__(message)
        # Затем свой код исключения
        self.errors_list = errors_list

    def __str__(self) -> Any:
        """."""
        return "Значение результата не подходит: " + str(self.errors_list)


class ZeroValueError(Exception):
    """."""

    def __init__(self, message: Any, errors_list: Any):
        """."""
        # Сначала вызов конструктора базового класса с параметрами которые ему нужны
        super().__init__(message)
        # Затем свой код исключения
        self.errors_list = errors_list

    def __str__(self) -> Any:
        """."""
        return "Повтор не предусмотрен: " + str(self.errors_list)
