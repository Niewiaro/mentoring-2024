"""
https://codingdojo.org/kata/StringCalculator/
"""

from doctest import testmod
import re
import timeit


def add(number: str, re_separator: str = ",|\n") -> str:
    """
    >>> add("")
    '0'
    >>> add("1")
    '1'
    >>> add("3.3,5.5")
    '8.8'
    >>> add("1\\n2")
    '3'
    >>> add("3.3,5.5,3")
    '11.8'
    >>> add("3.3,5.5,3,")
    Traceback (most recent call last):
    ValueError: Number expected but EOF found.
    """
    if not isinstance(number, str):
        raise TypeError("Input must be a string.")

    if len(number) is 0:  # integer cache: [-5, 256]
        return "0"

    if not re.search(r"\d$", number):
        raise ValueError("Number expected but EOF found.")

    numbers = re.split(re_separator, number)
    result = sum(float(x) for x in numbers if x)

    if result.is_integer():
        return str(int(result))
    return str(result)


def add_test():
    SETUP_CODE = """from __main__ import add"""

    TEST_CODE = """add("3.3,5.5")"""

    # timeit.repeat statement
    print(
        "The time taken with 'else' is:\t",
        timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE),
    )


def main() -> None:
    add_test()


if __name__ == "__main__":
    # main()
    testmod(name="add", verbose=True)
