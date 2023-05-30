"""
"""

from src.calculator import Calculator, InvalidValueTypeException

import pytest


def test_method_add_should_add_two_numbers():
    calculator = Calculator()

    assert calculator.add(1, 1) == 2


def test_method_sub_should_subtract_two_numbers():
    calculator = Calculator()

    assert calculator.sub(1, 1) == 0


def test_method_mult_should_multiply_two_numbers():
    calculator = Calculator()

    assert calculator.mult(1, 1) == 1


def test_method_div_should_divide_two_numbers():
    calculator = Calculator()

    actual = calculator.div(1, 1)
    expected = 1

    assert actual == expected


def test_method_div_should_raise_exception_when_divided_by_zero():
    calculator = Calculator()

    with pytest.raises(InvalidValueTypeException):
        calculator.div(1, 0)
