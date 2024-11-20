"""
https://codingdojo.org/kata/StringCalculator/
"""


def add(number: str, separator: str = ",") -> str:
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
        return result


def main() -> None:
    print("String Calculator")
    print(add(""))
    print(add("1"))
    print(add("1.1,2.2"))
    print(add("1.1,2.2,3.3"))


if __name__ == "__main__":
    main()
