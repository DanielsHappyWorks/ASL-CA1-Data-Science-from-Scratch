from src.utils.text_utils import TextUtils
from src.tests.test_helpers.std_in_out_helper import StdInOutHelper
import unittest


class TextUtilsTests(unittest.TestCase):
    """
        Tests check if different forms of yes returns true
    """
    def test_check_yes_valid_and_case_insensitive(self):
        self.check_valid_and_case_insensitive(TextUtils.checks_yes,
                                              ["y", "Y", "yes", "Yes", "yeS", "YeS", "YEs"])

    """
        Tests check if different forms of no returns true
    """
    def test_check_no_valid_and_case_insensitive(self):
        self.check_valid_and_case_insensitive(TextUtils.checks_no,
                                              ["n", "N", "no", "No", "nO", "NO"])

    """
        Tests check if different forms of integer returns true
    """
    def test_check_int_valid_and_case_insensitive(self):
        self.check_valid_and_case_insensitive(TextUtils.checks_int,
                                              ["i", "I", "int", "Int", "iNt", "integer", "Integer"])

    """
        Tests check if different forms of float returns true
    """
    def test_check_float_valid_and_case_insensitive(self):
        self.check_valid_and_case_insensitive(TextUtils.checks_float,
                                              ["f", "F", "float", "Float", "FloAT", "fLOaT", "fLOAt"])

    """
        Tests check if different forms of string returns true
    """
    def test_check_str_valid_and_case_insensitive(self):
        self.check_valid_and_case_insensitive(TextUtils.checks_str,
                                              ["s", "S", "str", "Str", "sTR", "string", "String","stRiNg", "sTriNG"])

    """
        Tests check if different strings return false if not what expected
    """
    def test_check_invalid_yes_values_return_false(self):
        self.check_invalid_string(TextUtils.checks_yes,
                                  ["n", "N", "no", "No", "nO", "NO",
                                   "i", "I", "int", "Int", "iNt", "integer", "Integer",
                                   "f", "F", "float", "Float", "FloAT", "fLOaT", "fLOAt",
                                   "s", "S", "str", "Str", "sTR", "string", "String", "stRiNg", "sTriNG"])

    """
        Tests check if different strings return false if not what expected
    """
    def test_check_invalid_no_values_return_false(self):
        self.check_invalid_string(TextUtils.checks_no,
                                  ["y", "Y", "yes", "Yes", "yeS", "YeS", "YEs"
                                   "i", "I", "int", "Int", "iNt", "integer", "Integer",
                                   "f", "F", "float", "Float", "FloAT", "fLOaT", "fLOAt",
                                   "s", "S", "str", "Str", "sTR", "string", "String", "stRiNg", "sTriNG"])

    """
        Tests check if different strings return false if not what expected
    """
    def test_check_invalid_int_values_return_false(self):
        self.check_invalid_string(TextUtils.checks_int,
                                  ["n", "N", "no", "No", "nO", "NO",
                                   "y", "Y", "yes", "Yes", "yeS", "YeS", "YEs",
                                   "f", "F", "float", "Float", "FloAT", "fLOaT", "fLOAt",
                                   "s", "S", "str", "Str", "sTR", "string", "String", "stRiNg", "sTriNG"])

    """
        Tests check if different strings return false if not what expected
     """
    def test_check_invalid_float_values_return_false(self):
        self.check_invalid_string(TextUtils.checks_float,
                                  ["y", "Y", "yes", "Yes", "yeS", "YeS", "YEs",
                                   "n", "N", "no", "No", "nO", "NO",
                                   "i", "I", "int", "Int", "iNt", "integer", "Integer",
                                   "s", "S", "str", "Str", "sTR", "string", "String", "stRiNg", "sTriNG"])

    """
        Tests check if different strings return false if not what expected
    """
    def test_check_invalid_string_values_return_false(self):
        self.check_invalid_string(TextUtils.checks_str,
                                  ["y", "Y", "yes", "Yes", "yeS", "YeS", "YEs",
                                   "n", "N", "no", "No", "nO", "NO",
                                   "i", "I", "int", "Int", "iNt", "integer", "Integer",
                                   "f", "F", "float", "Float", "FloAT", "fLOaT", "fLOAt"])
    """
        Tests the menu gets printed properly on new lines
    """
    def test_print_menu(self):
        self.assertEqual(StdInOutHelper.get_std_output_when_running_function(
            TextUtils.print_menu, ["1) a", "2) b", "3) c"]), "\n1) a\n2) b\n3) c\n")

    """
        Tests the dictionary gets printed properly as a table
    """
    def test_print_dictionary_as_table(self):
        self.assertEqual(StdInOutHelper.get_std_output_when_running_function(
            TextUtils.print_dict, {"A": [1, 2], "B": [3, 4]}), "A\t\tB\n1\t\t3\n2\t\t4\n")

    """
        Tests a function returns True with a specific string
        :param func
            Function to be called
        :param list_to_check
            list of strings to be checked
    """
    def check_valid_and_case_insensitive(self, func, list_to_check):
        for str_to_check in list_to_check:
            self.assertEqual(func(str_to_check), True)

    """
        Tests a function returns False with a specific string
        :param func
            Function to be called
        :param list_to_check
            list of strings to be checked
    """
    def check_invalid_string(self, func, list_to_check):
        for str_to_check in list_to_check:
            self.assertEqual(func(str_to_check), False)


if __name__ == '__main__':
    unittest.main()
