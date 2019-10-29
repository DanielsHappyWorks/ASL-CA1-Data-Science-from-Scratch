from DataFrame import DataFrame
from TextUtils import TextUtils

#TO DO
#   Catch invalid inputs for selections
#   catch invalid path
#   check the given path is a csv
#   add linear regression for 2 columns
#   add export for linear regression modal
#   add ability to plot the linear regression line with values
#   remove duplication
#   Update comments where necessary
#   Allow user specified delimiter


def main():
    while True:
        print()
        print("Linear Regression Program:")
        print("1) process build in data set:")
        print("2) load in data set:")
        print("3) Quit:")
        selection = int(input("Please select an option (0-2):"))
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
        print()
        print("1) print data set:")
        print("2) run linear regression on data set and print output:")
        print("3) run linear regression on data set and plot output:")
        print("4) run linear regression on data set and export output:")
        print("5) Back:")
        selection = int(input("Please select an option (0-2):"))
        if selection == 1:
            data_frame.print_data()
        elif selection == 2:
            print()
            data_frame.print_headings()
            x_axis = int(input("Please select the column (must be integer/float) for the x axis:"))
            y_axis = int(input("Please select the column (must be integer/float) for the y axis:"))
            data_frame.run_linear_regression(x_axis, y_axis)
            data_frame.print_linear_regression_output()
        elif selection == 4:
            print()
            data_frame.print_headings()
            x_axis = int(input("Please select the column (must be integer/float) for the x axis:"))
            y_axis = int(input("Please select the column (must be integer/float) for the y axis:"))
            file_name = input("Please specify a file directory and name i.e ./export.csv:")
            data_frame.run_linear_regression(x_axis, y_axis)
            data_frame.export_linear_regression_output()
        elif selection == 3:
            print()
            data_frame.print_headings()
            x_axis = int(input("Please select the column (integer) for the x axis:"))
            y_axis = int(input("Please select the column (integer) for the y axis:"))
            file_name = input("Please specify a file directory and name i.e ./export.csv:")
            data_frame.run_linear_regression(x_axis, y_axis)
            data_frame.export_linear_regression_output()
        elif selection == 5:
            break


main()
