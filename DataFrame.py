# TO DO
#   Add comments
#   Add linear regression algorithm
#   Add export for algorithm
#   Add conversion for values in set (int, float)
#   Add exclusion of errorous rows
#   Add tests
class DataFrame:
    data = dict()

    def __init__(self, headers, data_lines, defaults=[], delimiter=','):
        self.headers = headers
        self.defaults = defaults
        self.delimiter = delimiter
        for line in data_lines:
            fields = line.split(delimiter)
            for i, value in enumerate(fields):
                self.data.setdefault(headers[i].strip(), []).append(value.strip())

    def runLinearRegression(self, x_axis, y_axis):
        print("TO DO")

    def printLinearRegressionOutput(self):
        print("TO DO")

    def exportLinearRegressionOutput(self, file_name):
        print("TO DO")

    def printHeadings(self):
        print("TO DO")

    def printData(self):
        for row in zip(*([key] + (value) for key, value in self.data.items())):
            print(*row, sep='\t')
