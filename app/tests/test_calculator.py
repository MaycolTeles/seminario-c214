"""
"""

from app.src.calculator import Calculator


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

    assert calculator.div(1, 1) == 1
