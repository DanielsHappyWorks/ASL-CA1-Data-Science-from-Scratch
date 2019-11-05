# TO DO
#   Add comments
#   Add handling for FileIO
#       catch invalid path/file
#       check the given path is a csv


class ExceptionUtils:

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

    @staticmethod
    def convert_to_int(text):
        try:
            return int(text)
        except Exception as ex:
            print(f"Invalid Integer Conversion on value {text}. ERROR: {ex}")
            return False

    @staticmethod
    def convert_to_float(text):
        try:
            return float(text)
        except Exception as ex:
            print(f"Invalid Float Conversion on value {text}. ERROR: {ex}")
            return False
