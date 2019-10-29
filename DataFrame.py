from TextUtils import TextUtils
# TO DO
#   Add comments
#   Add linear regression algorithm
#   Add export for algorithm
#   Add tests
#   Update comments where necessary


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
        self.headers = headers
        self.data_types = data_types
        self.delimiter = delimiter
        for line in data_lines:
            fields = self.process_row(line.split(delimiter))
            if fields:
                for i, value in enumerate(fields):
                    self.data.setdefault(headers[i].strip(), []).append(value)

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
                if TextUtils.checks_int(self.data_types[i]):
                    processed_row.append(int(value.strip()))
                elif TextUtils.checks_str(self.data_types[i]):
                    processed_row.append(value.strip())
                elif TextUtils.checks_float(self.data_types[i]):
                    processed_row.append(float(value.strip()))
                else:
                    print(f"could not convert a value in the row, dropping row as data type is incorrect: {self.data_types[i]} index of value: {i}, value {value.strip()}, row: {row}")
                    return False
        return processed_row

    """
    Runs the linear regression algorithm on 2 columns in the data set
    """
    def run_linear_regression(self, x_axis, y_axis):
        print("TO DO")

    """
    prints the data from the linear regression to the console
    """
    def print_linear_regression_output(self):
        print("TO DO")

    """
    exports the data from the linear regression to a file
    """
    def export_linear_regression_output(self, file_name):
        print("TO DO")

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

    """
    Prints the data in the data frame to the console
    """
    def print_data(self):
        for row in zip(*([key] + list(map(str, value)) for key, value in self.data.items())):
            print(*row, sep='\t\t')
