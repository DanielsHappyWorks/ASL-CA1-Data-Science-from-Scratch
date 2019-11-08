import unittest
from unittest import mock
import io
import sys
from Utils.ExceptionUtils import ExceptionUtils


class ExceptionUtilsTests(unittest.TestCase):
    """
        Tests all of the edge cases for selecting out of a range get returned properly
    """
    def test_select_int_test_valid(self):
        mock.builtins.input = lambda _: "1"
        self.assertEqual(ExceptionUtils.select_int("Input Question", 1, 10), 1)
        mock.builtins.input = lambda _: "5"
        self.assertEqual(ExceptionUtils.select_int("Input Question", 1, 10), 5)
        mock.builtins.input = lambda _: "10"
        self.assertEqual(ExceptionUtils.select_int("Input Question", 1, 10), 10)

    """
        Tests invalid range is handled gracefully
    """
    def test_select_int_test_valid(self):
        mock.builtins.input = lambda _: "-234"
        self.assert_contains_stdout_and_return(ExceptionUtils.select_int,
                                               "Invalid Input, please try again. ERROR", "Input Question", 1, 10)

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
        self.assertFalse(self.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "12.0"))
        self.assertFalse(self.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "0.12"))
        self.assertFalse(self.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "-54.26"))

    """
        checks strings display an error and return false 
        so the program can handle incorrect conversions gracefully
    """
    def test_convert_to_int_with_string(self):
        self.assertFalse(self.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "str"))
        self.assertFalse(self.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
                                                                "Invalid Integer Conversion on value", "5we4r-3"))
        self.assertFalse(self.assert_contains_stdout_and_return(ExceptionUtils.convert_to_int,
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
    def test_convert_to_float_with_int_as_string(self):
        self.assertEqual(ExceptionUtils.convert_to_float("134.42"), 134.42)
        self.assertEqual(ExceptionUtils.convert_to_float("-23.689"), -23.689)
        self.assertEqual(ExceptionUtils.convert_to_float("0.123456789"), 0.123456789)

    """
        checks strings display an error and return false 
        so the program can handle incorrect conversions gracefully
    """
    def test_convert_to_int_with_string(self):
        self.assertFalse(self.assert_contains_stdout_and_return(ExceptionUtils.convert_to_float,
                                                                "Invalid Float Conversion on value", "str"))
        self.assertFalse(self.assert_contains_stdout_and_return(ExceptionUtils.convert_to_float,
                                                                "Invalid Float Conversion on value", "5we4r-3"))
        self.assertFalse(self.assert_contains_stdout_and_return(ExceptionUtils.convert_to_float,
                                                                "Invalid Float Conversion on value", "rd4572"))

    """
        Redirects stdout (print statements) to a variable, runs a function and Redirects stdout back to normal.
        Then evaluates the stdout against expected output by checking if actual contains expected and returns function output
        :param func
            function to be run between output redirection
        :param param
            parameter passed into the function
        :param expected
            string to evaluate stdout against
        :return output 
            returns the output from the function
    """
    def assert_contains_stdout_and_return(self, func, expected, param1=None, param2=None, param3=None):
        actual = io.StringIO()
        sys.stdout = actual
        if param3:
            output = func(param1, param2, param3)
        elif param2:
            output = func(param1, param2)
        elif param1:
            output = func(param1)
        else:
            output = func(param1)
        sys.stdout = sys.__stdout__
        print(f"{expected}: {actual.getvalue()}")
        self.assertTrue(expected in actual.getvalue())
        return output

    def user_inp(self, strin):
        sys.__stdin__


if __name__ == '__main__':
    unittest.main()
