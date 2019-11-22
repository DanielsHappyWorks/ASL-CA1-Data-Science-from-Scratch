from src.data_frame import DataFrame
from src.tests.test_helpers.std_in_out_helper import StdInOutHelper
import unittest


class DataFrameTests(unittest.TestCase):
    """
        Tests the headings in the data frame get printed correctly
    """
    def test_print_headings_with_type(self):
        data_frame = DataFrameTests.load_csv_test_data_valid()
        print_out = StdInOutHelper.get_std_output_when_running_function(data_frame.print_headings_with_type)
        expected_out = "header 0: A - int\n" \
                       "header 1: B - float\n" \
                       "header 2: C - int\n" \
                       "header 3: D - int\n"
        self.assertEqual(print_out, expected_out)

    """
        Tests that invalid rows will be dropped from the data frame and linear regression is still possible
    """
    def test_invalid_rows_get_dropped_from_data_frame(self):
        data_frame = DataFrameTests.load_csv_test_data_invalid()
        self.assertEqual(len(data_frame.data["A"]), 2)
        self.assertEqual(len(data_frame.data["B"]), 2)
        self.assertEqual(len(data_frame.data["C"]), 2)
        self.assertEqual(len(data_frame.data["D"]), 2)
        data_frame.run_linear_regression(0, 3)
        self.assertEqual(data_frame.slope, 1)
        self.assertEqual(data_frame.y_intercept, 0)
        self.assertEqual(data_frame.predicted_y, [1, 2])

    """
        Tests the mean, variance and std dev is printed correctly
    """
    def test_print_mean_variance_and_std_deviation(self):
        data_frame = DataFrameTests.load_csv_test_data_valid()
        print_out = StdInOutHelper.get_std_output_when_running_function(data_frame.print_deviation_calculations, 1)
        expected_out = "For Mean: The Standard Deviation is 19.30, The Variance is 372.31 and the Mean in 29.84\n" \
                       "For Median: The Standard Deviation is 19.30, The Variance is 372.64 and the Median in 30.41" \
                       "\nFor Mode: The Standard Deviation is 32.61, The Variance is 1063.47 and the Mode in 56.13\n"
        self.assertEqual(print_out, expected_out)

    """
        Tests the data from linear regression is printed correctly
    """
    def test_print_linear_regression_output_linear_regression(self):
        data_frame = DataFrameTests.load_csv_test_data_valid()
        data_frame.run_linear_regression(0, 1)
        print_out = StdInOutHelper.get_std_output_when_running_function(data_frame.print_linear_regression_output)
        expected_out = "A\t\tB\t\tPredicted Y\n" \
                       "1\t\t2.4\t\t9.363511450381678\n" \
                       "2\t\t25.7\t\t15.663969465648854\n" \
                       "6\t\t35.13\t\t40.86580152671756\n" \
                       "8\t\t56.13\t\t53.46671755725191\n" \
                       "Formula: Y = 6.300458015267177 * X + 3.063053435114501, slope of the line: " \
                       "6.300458015267177, Y Intercept of the Line 3.063053435114501\n"
        self.assertEqual(print_out, expected_out)

    """
        Tests the output of slope and y intercept from running linear regression on small data set
    """
    def test_slope_and_y_intercept_of_linear_regression(self):
        data_frame = DataFrameTests.load_csv_test_data_valid()
        data_frame.run_linear_regression(0, 1)
        self.assertEqual(data_frame.slope, 6.300458015267177)
        self.assertEqual(data_frame.y_intercept, 3.063053435114501)
        data_frame.run_linear_regression(0, 2)
        self.assertEqual(data_frame.slope, 3.2061068702290076)
        self.assertEqual(data_frame.y_intercept, -25.62595419847328)
        data_frame.run_linear_regression(0, 3)
        self.assertEqual(data_frame.slope, 0.3816793893129771)
        self.assertEqual(data_frame.y_intercept, 0.8778625954198471)

    """
        Tests the predictions made by linear regression
    """
    def test_predicted_y_values_from_linear_regression(self):
        data_frame = DataFrameTests.load_csv_test_data_valid()
        data_frame.run_linear_regression(0, 1)
        self.assertEqual(data_frame.predicted_y, [9.363511450381678, 15.663969465648854, 40.86580152671756, 53.46671755725191])
        data_frame.run_linear_regression(0, 2)
        self.assertEqual(data_frame.predicted_y, [-22.419847328244273, -19.213740458015266, -6.389312977099234, 0.02290076335878055])
        data_frame.run_linear_regression(0, 3)
        self.assertEqual(data_frame.predicted_y, [1.2595419847328242, 1.6412213740458013, 3.16793893129771, 3.931297709923664])

    """
        Loads the test.csv into a data frame object
    """
    @staticmethod
    def load_csv_test_data_valid():
        with open("./test_files/test.csv") as csv_data:
            headers = csv_data.readline().split(",")
            return DataFrame(headers, csv_data, ["int", "float", "int", "int"], ",")

    """
        Loads the test_invalid.csv into a data frame object incorrectly
    """
    @staticmethod
    def load_csv_test_data_invalid():
        with open("./test_files/test_invalid.csv") as csv_data:
            headers = csv_data.readline().split(",")
            return DataFrame(headers, csv_data, ["int", "float", "str", "int"], ",")


if __name__ == '__main__':
    unittest.main()
