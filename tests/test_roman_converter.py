import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.roman_converter import decimal_to_roman
import unittest


class TestRomanConverter(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

    def test_medium_numbers(self):
        self.assertEqual(decimal_to_roman(15), "XV")
        self.assertEqual(decimal_to_roman(58), "LVIII")  
        self.assertEqual(decimal_to_roman(2023), "MMXXIII")
        self.assertEqual(decimal_to_roman(1666), "MDCLXVI")  

    def test_high_numbers(self):
        self.assertEqual(decimal_to_roman(1987), "MCMLXXXVII")
        self.assertEqual(decimal_to_roman(2999), "MMCMXCIX")

    def test_lower_boundaries(self):
        self.assertEqual(decimal_to_roman(2), "II")
        self.assertEqual(decimal_to_roman(3), "III")
        self.assertEqual(decimal_to_roman(6), "VI")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            decimal_to_roman("100")
        with self.assertRaises(TypeError):
            decimal_to_roman(None)


if __name__ == '__main__':
    unittest.main()

