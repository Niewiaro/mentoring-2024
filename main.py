"""
https://codingdojo.org/kata/StringCalculator/
"""

from doctest import testmod
import re


def add(number: str, re_separator: str = ",|\n") -> str:
    """
    >>> add("")
    '0'
    >>> add("1")
    '1'
    >>> add("3.3,5.5")
    '8.8'
    >>> add("3.3,5.5,3")
    '11.8'
    >>> add("3.3,5.5,3,")
    'Number expected but EOF found.'
    """
    # >>> add("3.3\n5.5,3")
    # '11.8'

    if len(number) is 0:  # integer cache: [-5, 256]
        return "0"

    if not re.search(r"\d$", number):
        return "Number expected but EOF found."

    # numbers = number.split(separator)
    numbers = re.split(re_separator, number)
    if len(numbers) is 1:
        return numbers[0]
    else:  # Will function be faster without else?
        # numbers = [float(x) for x in numbers]

        result = 0
        for x in numbers:
            result += float(x)
        return str(result)


def main() -> None:
    print("String Calculator")


if __name__ == "__main__":
    main()
    testmod(name="add", verbose=True)
