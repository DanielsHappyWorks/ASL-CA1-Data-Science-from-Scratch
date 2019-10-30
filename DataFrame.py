from TextUtils import TextUtils
from ExceptionUtils import ExceptionUtils
import matplotlib.pyplot as pyplot
from MathsUtil import MathsUtil
from datetime import datetime
import os
# TO DO
#   Update comments where necessary
#   remove duplication


class DataFrame:
    data = dict()

    """
    Constructor for the DataFrame class
    :param headers
        defines the headers for the data
    :param data_lines 
        data containing all of the row information, rows with invalid values will be dropped 
    :param data_types
        specifies what each value per header should be converted to (string, integer, float),
        will assume all should be integers if not defined
    :param delimiter
        default delimiter for splitting the csv
    """
    def __init__(self, headers, data_lines, data_types=[], delimiter=','):
        self.headers = []
        for header in headers:
            self.headers.append(header.strip())
        self.data_types = data_types
        self.delimiter = delimiter
        for line in data_lines:
            fields = self.process_row(line.split(delimiter))
            if fields:
                for i, value in enumerate(fields):
                    self.data.setdefault(self.headers[i], []).append(value)

    """
    converts a row of data to the correct data type
    :param row
        takes the row to be processed as a specific data type
    :returns
        the converted row or false if the conversion failed
    """
    def process_row(self, row):
        processed_row = []
        if len(self.data_types) == 0:
            for value in row:
                processed_row.append(int(value.strip()))
        elif len(self.headers) != len(self.data_types):
            print(f"The amount of data types does not match the amount of headers, dropping row {row}")
            return False
        else:
            for i, value in enumerate(row):
                if TextUtils.checks_int(self.data_types[i]) and (ExceptionUtils.convert_to_int(value.strip()) or
                                                                 ExceptionUtils.convert_to_int(value.strip()) == 0):
                    processed_row.append(ExceptionUtils.convert_to_int(value.strip()))
                elif TextUtils.checks_str(self.data_types[i]):
                    processed_row.append(value.strip())
                elif TextUtils.checks_float(self.data_types[i]) and (ExceptionUtils.convert_to_float(value.strip()) or
                                                                 ExceptionUtils.convert_to_float(value.strip()) == 0):
                    processed_row.append(ExceptionUtils.convert_to_float(value.strip()))
                else:
                    print(f"could not convert a value in the row, dropping row as data type is incorrect: {self.data_types[i]} index of value: {i}, value {value.strip()}, row: {row}")
                    return False
        return processed_row

    """
    Runs the linear regression algorithm on 2 columns in the data set
    :param x_axis
        index of the column to be plotted against x
    :param y_axis
        index of the column to be plotted against y
    """
    def run_linear_regression(self, x_axis, y_axis):
        self.x_axis = self.headers[x_axis]
        self.y_axis = self.headers[y_axis]
        self.y_intercept = MathsUtil.estimate_y_intercept(self.data[self.x_axis], self.data[self.y_axis])
        self.slope = MathsUtil.estimate_slope(self.data[self.x_axis], self.data[self.y_axis], self.y_intercept)
        self.predicted_y = MathsUtil.num_plus_arr(self.slope, MathsUtil.num_by_arr(self.y_intercept, self.data[self.x_axis]))

    """
    prints the data from the linear regression to the console
    """
    def print_linear_regression_output(self):
        data_to_print = dict()
        data_to_print[self.x_axis] = self.data[self.x_axis]
        data_to_print[self.y_axis] = self.data[self.y_axis]
        data_to_print["Predicted Y"] = self.predicted_y
        TextUtils.print_dict(data_to_print)
        print(f"Formula: Y = {self.slope} * X + {self.y_intercept}, slope of the line: {self.slope}, Y Intercept of the Line {self.y_intercept}")

    """
    exports the data from the linear regression to a directory
    :param dir_name
        uses the specified directory to output files to
    """
    def export_linear_regression_output(self):
        date = datetime.now().strftime('%d-%m-%Y-%H-%M-%S')
        pyplot.scatter(self.data[self.x_axis], self.data[self.y_axis], color="b",
                       marker="x", s=40, label='points')
        pyplot.plot(self.data[self.x_axis], self.predicted_y, color="r", label='line')
        pyplot.xlabel(self.x_axis)
        pyplot.ylabel(self.y_axis)
        pyplot.title(f"{self.x_axis} vs {self.y_axis}")
        pyplot.legend()
        if not os.path.exists(f"./output/{date}/"):
            os.makedirs(f"./output/{date}/")
        pyplot.savefig(f"./output/{date}/{self.x_axis}_{self.y_axis}.png")

        file = open(f"./output/{date}/{self.x_axis}_{self.y_axis}.csv", "w")
        data_to_print = dict()
        data_to_print[self.x_axis] = self.data[self.x_axis]
        data_to_print[self.y_axis] = self.data[self.y_axis]
        data_to_print["Predicted Y"] = self.predicted_y
        for row in zip(*([key] + list(map(str, value)) for key, value in data_to_print.items())):
            file.write(','.join(row))
            file.write('\n')
        file.close()

        file = open(f"./output/{date}/{self.x_axis}_{self.y_axis}.txt", "w")
        file.write(f"Formula: Y = {self.slope} * X + {self.y_intercept}, slope of the line: {self.slope}, Y Intercept of the Line {self.y_intercept}")
        file.close()

    """
    displays the output of the linear regression run on screen
    """
    def plot_linear_regression_output(self):
        pyplot.scatter(self.data[self.x_axis], self.data[self.y_axis], color="b",
                       marker="x", s=40, label='points')
        pyplot.plot(self.data[self.x_axis], self.predicted_y, color="r", label='line')
        pyplot.xlabel(self.x_axis)
        pyplot.ylabel(self.y_axis)
        pyplot.title(f"{self.x_axis} vs {self.y_axis}")
        pyplot.legend()
        pyplot.show()

    """
    Prints the headings and defined data types for the data frame
    will print Errors data_types if there is a mismatch in data
    """
    def print_headings_with_type(self):
        for i, header in enumerate(self.headers):
            if len(self.data_types) == 0:
                print(f"header {i}: {header.strip()} - integer")
            elif len(self.headers) != len(self.data_types):
                print(f"header {i}: {header.strip()} - Errors data_types")
            else:
                print(f"header {i}: {header.strip()} - {self.data_types[i]}")
