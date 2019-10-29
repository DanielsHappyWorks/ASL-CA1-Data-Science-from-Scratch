class TextUtils:

    """
    checks if a string contains values yes or y
    :param value
        string to be tested
    """
    @staticmethod
    def checks_yes(value):
        return TextUtils.checks_text_in_array(value, ["y", "yes"])

    """
    checks if a string contains values no or n
    :param value
        string to be tested
    """
    @staticmethod
    def checks_no(value):
        return TextUtils.checks_text_in_array(value, ["n", "no"])

    """
    checks if a string contains values i, int or integer
    :param value
        string to be tested
    """
    @staticmethod
    def checks_int(value):
        return TextUtils.checks_text_in_array(value, ["i", "int", "integer"])

    """
    checks if a string contains values f or float
    :param value
        string to be tested
    """
    @staticmethod
    def checks_float(value):
        return TextUtils.checks_text_in_array(value, ["f", "float"])

    """
    checks if a string contains values s, str or string
    :param value
        string to be tested
    """
    @staticmethod
    def checks_str(value):
        return TextUtils.checks_text_in_array(value, ["s", "str", "string"])

    """
    checks if a string.lower() is present in an array
    :param value
        string to be tested
    :param array
        array which contains a list to be tested against
    """
    @staticmethod
    def checks_text_in_array(value, array):
        if value.lower() in array:
            return True
        return False

    """
    prints an array to screen
    :param menu_items
        array of strings to be printed to screen
    """
    @staticmethod
    def print_menu(menu_items):
        print()
        for item in menu_items:
            print(item)
