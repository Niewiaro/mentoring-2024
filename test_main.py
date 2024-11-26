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

    def test_float_and_int(self):
        self.assertAlmostEqual(float(add("3.3,5.5,3")), 11.8)

    def test_trailing_separator(self):
        self.assertRaises(ValueError, add, "1,2,3,")

    def test_types(self):
        self.assertRaises(TypeError, add, 1)
        self.assertRaises(TypeError, add, 3 + 5j)
        self.assertRaises(TypeError, add, True)

    def test_negative_numbers(self):
        self.assertEqual(add("-1,2"), "1")
        self.assertEqual(add("-1,-2"), "-3")

    def test_edge_cases(self):
        self.assertEqual(add("1,\n2"), "3")
        self.assertEqual(add(",,1,2"), "3")
        self.assertEqual(add("1,,2"), "3")

    def test_large_numbers(self):
        self.assertEqual(add("1000000000,2000000000"), "3000000000")


if __name__ == "__main__":
    unittest.main()
