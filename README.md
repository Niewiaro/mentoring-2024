# String Calculator with `unittest` and `doctest`

Welcome to the **String Calculator** project! This repository showcases my journey in exploring Python's testing frameworks: `unittest` and `doctest`. The implementation follows the [String Calculator Kata](https://codingdojo.org/kata/StringCalculator/) with additional features.

## Features

- **Addition of Numbers**: Supports integers and floats, separated by commas or newlines.
- **Custom Error Handling**: Validates input format and raises descriptive exceptions.
- **Extensive Testing**:
  - `doctest`: Inline examples to ensure correctness during development.
  - `unittest`: Comprehensive test cases for edge scenarios.

---

## File Structure

### `main.py`

This file implements the core functionality:

- `add(number: str, re_separator: str = ",|\n") -> str`  
  Adds numbers from a delimited string.  
  Example usage (validated via `doctest`):
  ```python
  >>> add("1,2")
  '3'
  >>> add("1.5,2.5")
  '4.0'
  ```

- Error handling:
  - Empty string → Returns `'0'`.
  - Trailing separator → Raises `ValueError`.
  - Non-string input → Raises `TypeError`.

- Benchmarking utility with `timeit`.

### `test_main.py`

Contains test cases written using `unittest`:

- Validates core functionalities.
- Tests edge cases:
  - Mixed separators.
  - Trailing or missing separators.
  - Negative numbers.
  - Large numbers.
  - Incorrect input types.

---

## How to Run

### Running `doctest`

To validate inline examples using `doctest`:
```bash
python main.py
```

### Running `unittest`

To execute unit tests:
```bash
python -m unittest test_main.py
```

---

## Example Use Case

```python
from main import add

# Add numbers from a string
result = add("10,20,30")
print(result)  # Output: '60'

# Handle floats
result = add("1.1,2.2,3.3")
print(result)  # Output: '6.6'
```

---

## Project Goals

1. **Learn `doctest`**: Write self-validating examples within the function docstrings.
2. **Explore `unittest`**: Build robust test suites for various scenarios.
3. **Practice Error Handling**: Create descriptive and user-friendly exceptions.

---

## Feedback & Contributions

I welcome feedback and suggestions for improving the implementation or test coverage. Feel free to open an issue or a pull request!

---

Thank you for visiting! 🎉
