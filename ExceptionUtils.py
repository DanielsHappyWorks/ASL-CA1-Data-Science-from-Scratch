# TO DO
#   Add handling for FileIO
#       catch invalid path/file
#       check the given path is a csv


class ExceptionUtils:
    """
        gets the next input and validates its an integer between a certain range. If it fails it tries again.
        :param text
            text to be used while asking for input
        :param low
            the lowest value that can be used
        :param high
            the highest value that can be used
        :return int
            the value that was selected in the range
    """
    @staticmethod
    def select_int(text, low, high):
        try:
            selected_int = int(input(text))
            if selected_int < low:
                raise Exception(f'input was {selected_int} < {low}')
            if selected_int > high:
                raise Exception(f'input was {selected_int} > {high}')
            return selected_int
        except Exception as ex:
            print(f"Invalid Input, please try again. ERROR: {ex}")
            return ExceptionUtils.select_int(text, low, high)

    """
        converts text to integer.
        :param text
            text to be converted
        :return int/False
            returns the int value unless the conversion fails, then it returns False
    """
    @staticmethod
    def convert_to_int(text):
        try:
            return int(text)
        except Exception as ex:
            print(f"Invalid Integer Conversion on value {text}. ERROR: {ex}")
            return False

    """
        converts text to float.
        :param text
            text to be converted
        :return float/False
            returns the int value unless the conversion fails, then it returns False
    """
    @staticmethod
    def convert_to_float(text):
        try:
            return float(text)
        except Exception as ex:
            print(f"Invalid Float Conversion on value {text}. ERROR: {ex}")
            return False
