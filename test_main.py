import unittest
from main import add


class TestAdd(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), "0")

    def test_single_number(self):
        self.assertEqual(add("0"), "0")
        self.assertEqual(add("1"), "1")

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), "3")

    def test_float_numbers(self):
        self.assertAlmostEqual(float(add("1.1,2.2")), 3.3)

    def test_newline_separator(self):
        self.assertEqual(add("1\n2"), "3")

    def test_mixed_separators(self):
        self.assertEqual(add("1,2\n3"), "6")

    def test_trailing_separator(self):
        self.assertEqual(add("1,2,"), "Number expected but EOF found.")

    def test_float_and_int(self):
        self.assertAlmostEqual(float(add("3.3,5.5,3")), 11.8)


if __name__ == "__main__":
    unittest.main()
