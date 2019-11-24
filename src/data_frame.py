from src.utils.text_utils import TextUtils
from src.utils.exception_utils import ExceptionUtils
from src.utils.graph_utils import GraphUtils
from src.utils.maths_util import MathsUtil
import src.constant as constant
from datetime import datetime
import os


class DataFrame:
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
        self.data = dict()
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
                if not ExceptionUtils.convert_to_int(value.strip()) is None:
                    processed_row.append(ExceptionUtils.convert_to_int(value.strip()))
                else:
                    print(f"could not convert a value in the row, dropping row as data type is incorrect: int, value {value.strip()}, row: {row}")
                    return False
        elif len(self.headers) != len(self.data_types):
            print(f"The amount of data types does not match the amount of headers, dropping row {row}")
            return False
        else:
            for i, value in enumerate(row):
                if TextUtils.checks_int(self.data_types[i]) and not ExceptionUtils.convert_to_int(value.strip()) is None:
                    processed_row.append(ExceptionUtils.convert_to_int(value.strip()))
                elif TextUtils.checks_str(self.data_types[i]):
                    processed_row.append(value.strip())
                elif TextUtils.checks_float(self.data_types[i]) and not ExceptionUtils.convert_to_float(value.strip()) is None:
                    processed_row.append(ExceptionUtils.convert_to_float(value.strip()))
                else:
                    print(f"could not convert a value in the row, dropping row as data type is incorrect: {self.data_types[i]} index of value: {i}, value {value.strip()}, row: {row}")
                    return False
        return processed_row

    """
        The function prints the average, variance and standard deviation for mean, median and mode to screen
        :param column
            The id of the column in the data set
    """
    def print_deviation_calculations(self, column):
        rows = self.data[self.headers[column]]
        DataFrame.print_deviation_calculation("Mean", rows, MathsUtil.arr_mean(rows))
        DataFrame.print_deviation_calculation("Median", rows, MathsUtil.arr_median(rows))
        DataFrame.print_deviation_calculation("Mode", rows, MathsUtil.arr_mode(rows))

    """
        The function prints the average, variance and standard deviation for mean, median and mode to screen
        :param type
            String defining the type of average
        :param rows
            rows used to calculate variance and std
        :param average
            the value of the average for the set of rows
    """
    @staticmethod
    def print_deviation_calculation(average_type, rows, average):
        variance = MathsUtil.arr_variance(rows, average)
        standard_deviation = MathsUtil.arr_standard_deviation(rows, average)
        print(f"For {average_type}: The Standard Deviation is {standard_deviation:.2f}, The Variance is {variance:.2f} and the {average_type} in {average:.2f}")

    """
        The function plots a normal distribution and displays it on the screen
        :param column
            The id of the column in the data set
    """
    def plot_normal_distribution(self, column):
        mean = MathsUtil.arr_mean(self.data[self.headers[column]])
        median = MathsUtil.arr_median(self.data[self.headers[column]])
        mode = MathsUtil.arr_mode(self.data[self.headers[column]])
        GraphUtils.show_distribution_graph(self.data[self.headers[column]], self.headers[column], mean, median, mode)

    """
        exports the data from the distribution to a directory
        :param column
            column to be exported
        :param date
            uses the specified directory to output files to
    """
    def export_normal_distribution(self, column, date):
        path = DataFrame.get_export_path(date)
        mean = MathsUtil.arr_mean(self.data[self.headers[column]])
        median = MathsUtil.arr_median(self.data[self.headers[column]])
        mode = MathsUtil.arr_mode(self.data[self.headers[column]])
        GraphUtils.export_distribution_graph(self.data[self.headers[column]], self.headers[column],
                                             mean, median, mode, path)
        print(f"exported {path}dist_{self.headers[column]}")

    """
        exports the data from the distribution to a directory for all columns
    """
    def export_all_normal_distribution(self):
        date = datetime.now().strftime(constant.DATE_FOTMAT)
        for i, header in enumerate(self.headers):
            if len(self.data_types) == 0 or not TextUtils.checks_str(self.data_types[i]):
                self.export_normal_distribution(i, date)

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
        self.slope = MathsUtil.estimate_slope(self.data[self.x_axis], self.data[self.y_axis])
        self.y_intercept = MathsUtil.estimate_y_intercept(self.data[self.x_axis], self.data[self.y_axis], self.slope)
        self.predicted_y = MathsUtil.num_plus_arr(self.y_intercept, MathsUtil.num_by_arr(self.slope, self.data[self.x_axis]))

    """
        prints the data from the linear regression to the console
    """
    def print_linear_regression_output(self):
        data_to_print = dict()
        data_to_print[self.x_axis] = self.data[self.x_axis]
        data_to_print[self.y_axis] = self.data[self.y_axis]
        data_to_print[constant.PREDICTION_EXPORT_COL] = self.predicted_y
        TextUtils.print_dict(data_to_print)
        print(f"Formula: Y = {self.slope} * X + {self.y_intercept}, slope of the line: {self.slope}, Y Intercept of the Line {self.y_intercept}")

    """
        exports the data from the linear regression to a directory
        :param date
            uses the specified directory to output files to
    """
    def export_linear_regression_output(self, date):
        path = DataFrame.get_export_path(date)
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception as ex:
            print(f"Could't make path {path} Exception: {ex}")

        GraphUtils.export_linear_regression_graph(self.data, self.x_axis, self.y_axis, self.predicted_y, path)
        self.export_predicted_y_to_csv(path)
        self.export_predicted_line_data(path)
        print(f"exported {path}lr_{self.x_axis}_{self.y_axis}")

    """
        exports the slope, y intercept and formula of the predicted line 
        :param path
            the path the txt file should be created in
    """
    def export_predicted_line_data(self, path):
        try:
            with open(f"{path}lr_{self.x_axis}_{self.y_axis}.txt", "w") as file:
                file.write(
                    f"Formula: Y = {self.slope} * X + {self.y_intercept}, slope of the line: {self.slope}, Y Intercept of the Line {self.y_intercept}")
        except Exception as ex:
            print(f"Could't export predicted y values to {path}lr_{self.x_axis}_{self.y_axis}.txt Exception: {ex}")

    """
        exports the x, y and predicted y columns to a new csv file
        :param path
            the path the csv file should be created in
    """
    def export_predicted_y_to_csv(self, path):
        try:
            with open(f"{path}lr_{self.x_axis}_{self.y_axis}.csv", "w") as file:
                data_to_print = dict()
                data_to_print[self.x_axis] = self.data[self.x_axis]
                data_to_print[self.y_axis] = self.data[self.y_axis]
                data_to_print[constant.PREDICTION_EXPORT_COL] = self.predicted_y
                for row in zip(*([key] + list(map(str, value)) for key, value in data_to_print.items())):
                    file.write(','.join(row))
                    file.write('\n')
        except Exception as ex:
            print(f"Could't export predicted y values to {path}lr_{self.x_axis}_{self.y_axis}.csv Exception: {ex}")

    """
        displays the output of the linear regression run on screen
    """
    def plot_linear_regression_output(self):
        GraphUtils.show_linear_regression_graph(self.data, self.x_axis, self.y_axis, self.predicted_y)

    """
        export all combinations of Linear Regression in one go
    """
    def export_linear_regression_output_all(self):
        date = datetime.now().strftime(constant.DATE_FOTMAT)
        for i, header1 in enumerate(self.headers):
            for j, header2 in enumerate(self.headers):
                if not header1 == header2 and (len(self.data_types) == 0 or (not TextUtils.checks_str(self.data_types[i]) and not TextUtils.checks_str(self.data_types[j]))):
                    self.run_linear_regression(i, j)
                    self.export_linear_regression_output(date)

    """
        Prints the headings and defined data types for the data frame
        will print Errors data_types if there is a mismatch in data
    """
    def print_headings_with_type(self):
        for i, header in enumerate(self.headers):
            if len(self.data_types) == 0:
                print(f"header {i}: {header} - integer")
            elif len(self.headers) != len(self.data_types):
                print(f"header {i}: {header} - Errors data_types")
            else:
                print(f"header {i}: {header} - {self.data_types[i]}")

    """
        Sets the export path and tries to create the directory if not exists
        :param date
            date to use as part of the path name
        :return path 
            as string
    """
    @staticmethod
    def get_export_path(date):
        path = f"./output/{date}/"

        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except Exception as ex:
            print(f"Could't make path {path} Exception: {ex}")

        return path
