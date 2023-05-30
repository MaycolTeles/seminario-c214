"""
"""

from __future__ import annotations
from typing import Callable


class InvalidValueTypeException(Exception):
    """
    """

    def __init__(self, value: float) -> None:
        """
        """
        self.value = value

    def __str__(self) -> str:
        """
        """
        value = self.value
        value_type = type(value)

        string = f'Type of value "{value}" is "{value_type}" but it should be "float".'
        return string


def validate_arguments(
    function: Callable[[Calculator, float, float], float]
) -> Callable[[Calculator, float, float], float]:
    """
    """

    def wrapper(calculator: Calculator, value_1: float, value_2: float) -> float:
        """
        """
        value_1_is_valid = isinstance(value_1, float) or isinstance(value_1, int)

        if not value_1_is_valid:
            raise InvalidValueTypeException(value_1)

        value_2_is_valid = isinstance(value_2, float) or isinstance(value_1, int)

        if not value_2_is_valid:
            raise InvalidValueTypeException(value_2)

        return function(calculator, value_1, value_2)

    return wrapper


class Calculator:
    """
    """

    @validate_arguments
    def add(self, value_1: float, value_2: float) -> float:
        """
        """
        return value_1 + value_2

    @validate_arguments
    def sub(self, value_1: float, value_2: float) -> float:
        """
        """
        return value_1 - value_2

    @validate_arguments
    def mult(self, value_1: float, value_2: float) -> float:
        """
        """
        return value_1 * value_2

    @validate_arguments
    def div(self, value_1: float, value_2: float) -> float:
        """
        """
        if value_2 == 0:
            raise ZeroDivisionError("Divison by 0 not allowed!")

        return value_1 / value_2

    @validate_arguments
    def expo(self, value_1: float, value_2: float) -> float:
        """
        """
        # if value_2 == 0:
        #     return 1

        return value_1 ** value_2
