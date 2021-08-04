"""ValidAll - универсальный декоратор для валидации входных и выходных параметров функции."""

from typing import Callable, Any


def valid_all(input_validation: Any, result_validation: Any, on_fail_repeat_times: int,
              default_behavior: Any) -> Callable:
    """Декоратор."""
    def my_decorator(func: Any) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                if input_validation:
                    print("Исходные параметры прошли проверку.")
                    for i in range(0, abs(on_fail_repeat_times) + 1):
                        while True:
                            result = func(*args, **kwargs)
                            if result_validation:
                                break
                            else:
                                err = Exception("ResultVerificationError. Попытка: ", i)
                                print(err)
                                if on_fail_repeat_times < 0:
                                    continue
                                else:
                                    break

                        try:
                            if on_fail_repeat_times == 0:
                                raise ResultVerificationError("exception occur",
                                                              ["Попробуй другие данные."])
                        except ResultVerificationError:
                            print(ResultVerificationError("exception occur",
                                                          ["Попробуй другие данные."]))
                            break
                        if on_fail_repeat_times == i:
                            print(default_behavior)
                            break
                        elif result_validation:
                            print("Результат прошел проверку.")
                            return result

                else:
                    raise InputParameterVerificationError("exception occur",
                                                          ["Попробуй другие данные."])

            except InputParameterVerificationError:
                print(InputParameterVerificationError("exception occur",
                                                      ["Попробуй другие данные."]))

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


# можно протестировать работоспособность валидатора,раскомментировав строки 86-94.
# @valid_all(input_validation=True, result_validation=True,
#            on_fail_repeat_times=1, default_behavior=None)
# def foo(*args: Any, **kwargs: Any) -> Any:
#     """Исходная функция."""
#     return Any
#
#
# foo()
