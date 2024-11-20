"""
https://codingdojo.org/kata/StringCalculator/
"""

from doctest import testmod


def add(number: str, separator: str = ",") -> str:
    """
    >>> add("")
    '0'
    >>> add("1")
    '1'
    >>> add("3.3,5.5")
    '8.8'
    """
    if len(number) is 0:  # integer cache: [-5, 256]
        return "0"

    numbers = number.split(separator)
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
