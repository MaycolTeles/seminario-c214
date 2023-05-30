"""
"""

from calculator import Calculator


def main() -> None:
    """
    """
    calculator = Calculator()

    sum = calculator.add(3, 2)
    print("SOMA: ", sum)

    sub = calculator.sub(3, 2)
    print("SUBTRAÇÃO: ", sub)

    mult = calculator.mult(3, 2)
    print("MULTIPLICAÇÃO: ", mult)

    div = calculator.div(3, 2)
    print("DIVISÃO: ", div)


if __name__ == "__main__":
    main()
