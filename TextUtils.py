class TextUtils:

    @staticmethod
    def checks_yes(value):
        if value.lower() in ['yes', 'y']:
            return True
        return False

    @staticmethod
    def checks_no(value):
        if value.lower() in ['no', 'n']:
            return True
        return False

    @staticmethod
    def checks_int(value):
        if value.lower() == "i" or value.lower() == "int" or value.lower() == "integer":
            return True
        return False

    @staticmethod
    def checks_float(value):
        if value.lower() == "f" or value.lower() == "float":
            return True
        return False

    @staticmethod
    def checks_str(value):
        if value.lower() == "str" or value.lower() == "s" or value.lower() == "string":
            return True
        return False
