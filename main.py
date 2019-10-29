from DataFrame import DataFrame
from TextUtils import TextUtils
from ExceptionUtils import ExceptionUtils

# TO DO
#   add linear regression for 2 columns
#   add export for linear regression modal
#   add ability to plot the linear regression line with values
#   remove duplication
#   Update comments where necessary
#   Allow user specified delimiter
#   Add comments


def main():
    while True:
        TextUtils.print_menu(['Linear Regression Program:',
                              '1) process build in data set:',
                              '2) load in data set:',
                              '3) Quit:'])
        selection = ExceptionUtils.select_int("Please select an option (1-3):")
        if selection == 1:
            print("Opening CSV ./DataSet/hour.csv")
            data_frame = create_data_frame('./DataSet/hour.csv', ['int', 'str', 'int', 'int', 'int', 'int', 'int',
                                                                  'int', 'int', 'int', 'float', 'float',
                                                                  'float', 'float', 'int', 'int', 'int'])
            use_data_frame(data_frame)
        elif selection == 2:
            path = input("Please enter the path to the file:")
            print(f"Opening CSV {path}")
            data_frame = create_data_frame(path)
            use_data_frame(data_frame)
        elif selection == 3:
            break


def create_data_frame(path, data_types=[]):
    csv_data = open(path)
    headers = csv_data.readline().split(",")
    data_types = define_data_types(data_types, headers)
    return DataFrame(headers, csv_data, data_types, ',')


def define_data_types(data_types, headers):
    if len(data_types) == 0:
        while True:
            all_int = input("Are all of the columns integer values? (y/n)")
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
            print("please enter a valid input! (y, yes, n, no)")
    else:
        return data_types


def use_data_frame(data_frame):
    while True:
        TextUtils.print_menu(['1) print data set:',
                              '2) print header details:',
                              '3) run linear regression on data set and print output:',
                              '4) run linear regression on data set and plot output:',
                              '5) run linear regression on data set and export output:',
                              '6) Back:'])
        selection = ExceptionUtils.select_int("Please select an option (1-6):")
        if selection == 1:
            data_frame.print_data()
        elif selection == 2:
            data_frame.print_headings_with_type()
        elif selection == 3:
            print()
            data_frame.print_headings_with_type()
            x_axis = ExceptionUtils.select_int("Please select the column (must be integer/float) for the x axis:")
            y_axis = ExceptionUtils.select_int("Please select the column (must be integer/float) for the y axis:")
            data_frame.run_linear_regression(x_axis, y_axis)
            data_frame.print_linear_regression_output()
        elif selection == 4:
            print()
            data_frame.print_headings_with_type()
            x_axis = ExceptionUtils.select_int("Please select the column (must be integer/float) for the x axis:")
            y_axis = ExceptionUtils.select_int("Please select the column (must be integer/float) for the y axis:")
            file_name = input("Please specify a file directory and name i.e ./export.csv:")
            data_frame.run_linear_regression(x_axis, y_axis)
            data_frame.export_linear_regression_output()
        elif selection == 5:
            print()
            data_frame.print_headings_with_type()
            x_axis = ExceptionUtils.select_int("Please select the column (integer) for the x axis:")
            y_axis = ExceptionUtils.select_int("Please select the column (integer) for the y axis:")
            file_name = input("Please specify a file directory and name i.e ./export.csv:")
            data_frame.run_linear_regression(x_axis, y_axis)
            data_frame.export_linear_regression_output()
        elif selection == 6:
            break


main()
