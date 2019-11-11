from unittest import mock
import io
import sys


class StdInOutHelper:
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
    @staticmethod
    def assert_contains_stdout_and_return(func, expected, param1=None, param2=None, param3=None):
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
        assert expected in actual.getvalue()
        return output

    """
        Mocks the next stdin input
    """
    @staticmethod
    def mock_input(user_input):
        mock.builtins.input = lambda _: user_input