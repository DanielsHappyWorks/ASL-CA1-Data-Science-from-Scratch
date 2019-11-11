from src.data_frame import DataFrame
from src.utils.text_utils import TextUtils
from src.utils.exception_utils import ExceptionUtils
import src.constant as constant

"""
    runs when the program is started
    This method opens the first menu in the application
"""
def main():
    while True:
        TextUtils.print_menu(constant.MENU_SELECT_DATA_SET)
        selection = ExceptionUtils.select_int(constant.MENU_SELECT_DATA_SET_INPUT, 1, 3)
        if selection == 1:
            print(f"Opening CSV {constant.DEFAULT_DATA_SET_FILE}")
            data_frame = create_data_frame(constant.DEFAULT_DATA_SET_FILE, ",", constant.DEFAULT_DATA_SET_DATA_TYPES)
            if data_frame:
                use_data_frame(data_frame)
        elif selection == 2:
            path = input(constant.ENTER_PATH)
            delimiter = input(constant.ENTER_DELIMITER)
            print(f"Opening CSV {path}")
            data_frame = create_data_frame(path, delimiter)
            if data_frame:
                use_data_frame(data_frame)
        elif selection == 3:
            break


"""
    creates a DataFrame object from a csv to process in Linear Regression
    :param path
        string defining which csv to open
    :param data_types
        allows for programatical allocation of data types in the data set
    :return DataFrame
        returns a DataFrame object with the loaded data set
        If an exception is thrown while loading the data set the returned value will be false
"""
def create_data_frame(path, delimeter, data_types=[]):
    try:
        with open(path) as csv_data:
            headers = csv_data.readline().split(delimeter)
            data_types = define_data_types(data_types, headers)
            return DataFrame(headers, csv_data, data_types, delimeter)
    except Exception as ex:
        print(f"Could't load DataFrame at path {path} Exception: {ex}")
        return False


"""
    gets the data types for every column from the user
    :param data_types
        if defined will skip the process
    :param headers
        list of headers data is needed for
    :returns list
        list off data types that can be used to assign columns to correct types
"""
def define_data_types(data_types, headers):
    if len(data_types) == 0:
        while True:
            all_int = input(constant.ARE_ALL_INTEGERS)
            if TextUtils.checks_yes(all_int):
                return []
            elif TextUtils.checks_no(all_int):
                for header in headers:
                    while True:
                        header_type = input(f"what is the type of the column {header}? (int, float, string)")
                        if TextUtils.checks_int(header_type) or TextUtils.checks_str(header_type) or TextUtils.checks_float(header_type):
                            data_types.append(header_type.lower())
                            break
                        print(f"please enter a valid input for {header}! (int, float, string)")
                return data_types
            print(constant.INVALID_YES_NO)
    else:
        return data_types


"""
    After importing a data set this function allows the user to choose how to process it
    :param data_frame
        defines the loaded data in ram that can be used to run Linear Regression
"""
def use_data_frame(data_frame):
    while True:
        TextUtils.print_menu(constant.MENU_USE_DATA_SET)
        selection = ExceptionUtils.select_int(constant.MENU_USE_DATA_SET_INPUT, 1, 7)
        if selection == 1:
            TextUtils.print_dict(data_frame.data)
        elif selection == 2:
            data_frame.print_headings_with_type()
        elif selection == 3:
            run_regression(data_frame)
            data_frame.print_linear_regression_output()
        elif selection == 4:
            run_regression(data_frame)
            data_frame.export_linear_regression_output()
        elif selection == 5:
            run_regression(data_frame)
            data_frame.plot_linear_regression_output()
        elif selection == 6:
            data_frame.export_linear_regression_output_all()
        elif selection == 7:
            break


"""
    gets the columns to run Linear Regression on and processes the data set
    :param data_frame
        defines the data to run Linear Regression on
"""
def run_regression(data_frame):
    print()
    data_frame.print_headings_with_type()
    x_axis = get_valid_axis(constant.GET_AXIS_X, data_frame)
    y_axis = get_valid_axis(constant.GET_AXIS_Y, data_frame)
    data_frame.run_linear_regression(x_axis, y_axis)


"""
    takes user inputs until they select a valid column for Linear Regression
    :param text
        text displayed when getting a specific axis
    :param data_frame
        defines the data to run Linear Regression on
    :return int
        returns the selected index of the column for Linear Regression
"""
def get_valid_axis(text, data_frame):
    while True:
        axis = ExceptionUtils.select_int(text, 0, len(data_frame.headers)-1)
        if len(data_frame.data_types) == 0:
            return axis
        elif TextUtils.checks_int(data_frame.data_types[axis]):
            return axis
        print(f"Invalid Selection {axis}, Please select column of type Integer")


"""
    only triggers main when this file is called
"""
if __name__ == '__main__':
    main()
