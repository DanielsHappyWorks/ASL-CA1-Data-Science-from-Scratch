from src.Utils.ExceptionUtils import ExceptionUtils
from src.tests.TestHelpers.StdInOutHelper import StdInOutHelper
import unittest


class ExceptionUtilsTests(unittest.TestCase):
    """
        Tests all of the edge cases for selecting out of a range get returned properly
    """
    def test_select_int_test_valid(self):
        StdInOutHelper.mock_input('1')
        self.assertEqual(ExceptionUtils.select_int("Input Question", 1, 10), 1)
        StdInOutHelper.mock_input('5')
        self.assertEqual(ExceptionUtils.select_int("Input Question", 1, 10), 5)
        StdInOutHelper.mock_input('10')
        self.assertEqual(ExceptionUtils.select_int("Input Question", 1, 10), 10)

    """
        checks positive and negative integers are converted correctly from strings
    """
    def test_convert_to_int_with_int_as_string(self):
        self.assertEqual(ExceptionUtils.convert_to_int("148"), 148)
        self.assertEqual(ExceptionUtils.convert_to_int("0"), 0)
        self.assertEqual(ExceptionUtils.convert_to_int("-482"), -482)

    """
        checks positive and negative floats display an error and return false 
        so the program can handle incorrect conversions gracefully
    """
    def test_convert_to_int_with_float_as_string(self):
        self.assertFalse(StdInOutHelper.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "12.0"))
        self.assertFalse(StdInOutHelper.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "0.12"))
        self.assertFalse(StdInOutHelper.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "-54.26"))

    """
        checks strings display an error and return false 
        so the program can handle incorrect conversions gracefully
    """
    def test_convert_to_int_with_string(self):
        self.assertFalse(StdInOutHelper.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "str"))
        self.assertFalse(StdInOutHelper.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "5we4r-3"))
        self.assertFalse(StdInOutHelper.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "rd4572"))

    """
        checks positive and negative integers are converted correctly from strings to floats
    """
    def test_convert_to_float_with_int_as_string(self):
        self.assertEqual(ExceptionUtils.convert_to_float("134"), 134.0)
        self.assertEqual(ExceptionUtils.convert_to_float("-23"), -23.0)
        self.assertEqual(ExceptionUtils.convert_to_float("0"), 0.0)

    """
        checks positive and negative floats are converted correctly from strings to floats
    """
    def test_convert_to_float_with_float_as_string(self):
        self.assertEqual(ExceptionUtils.convert_to_float("134.42"), 134.42)
        self.assertEqual(ExceptionUtils.convert_to_float("-23.689"), -23.689)
        self.assertEqual(ExceptionUtils.convert_to_float("0.123456789"), 0.123456789)

    """
        checks strings display an error and return false 
        so the program can handle incorrect conversions gracefully
    """
    def test_convert_to_float_with_string(self):
        self.assertFalse(StdInOutHelper.assert_contains_stdout_and_return(ExceptionUtils.convert_to_float,
                                                                "Invalid Float Conversion on value", "str"))
        self.assertFalse(StdInOutHelper.assert_contains_stdout_and_return(ExceptionUtils.convert_to_float,
                                                                "Invalid Float Conversion on value", "5we4r-3"))
        self.assertFalse(StdInOutHelper.assert_contains_stdout_and_return(ExceptionUtils.convert_to_float,
                                                                "Invalid Float Conversion on value", "rd4572"))


if __name__ == '__main__':
    unittest.main()
