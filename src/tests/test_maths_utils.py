from src.utils.maths_util import MathsUtil
import unittest


class MathsUtilsTests(unittest.TestCase):
    """
        Tests that the list is added correctly with positive, negative anf floating point numbers
    """
    def test_sum_of_array(self):
        self.assertEqual(MathsUtil.arr_sum([1, 2, 3]), 6)
        self.assertEqual(MathsUtil.arr_sum([1, -2, -3]), -4)
        self.assertEqual(MathsUtil.arr_sum([1, 2.6, 3.07]), 6.67)

    """
        Tests that the mean of a list is calculated correctly
    """
    def test_mean_of_array(self):
        self.assertEqual(MathsUtil.arr_mean([1, 2, 3]), 2)
        self.assertEqual(MathsUtil.arr_mean([14, -2, -3]), 3)
        self.assertEqual(MathsUtil.arr_mean([1, 2.6, 3.07, 2.3524]), 2.2556)

    """
        Tests that 2 lists are multiplied by each other correctly
    """
    def test_array_by_array(self):
        self.assertEqual(MathsUtil.arr_by_arr([1, 2, 3], [1, 0, 3]), [1, 0, 9])
        self.assertEqual(MathsUtil.arr_by_arr([-1, -2, -3], [-1, 2, 3]), [1, -4, -9])
        self.assertEqual(MathsUtil.arr_by_arr([2, 2.6, 3.02], [1.5, 2, 3]), [3, 5.2, 9.06])

    """
        Test that arrays of different lengths will not be multiplied
    """
    def test_array_by_array(self):
        self.assertEqual(MathsUtil.arr_by_arr([1, 2, 3], [1, 0, 3, 5]), [])
        self.assertEqual(MathsUtil.arr_by_arr([-1, -2, -3, 4], [-1, 2, 3]), [])

    """
        Tests that a number is multiplied by a list correctly
    """
    def test_number_by_array(self):
        self.assertEqual(MathsUtil.num_by_arr(0, [1, 2, 3]), [0, 0, 0])
        self.assertEqual(MathsUtil.num_by_arr(2, [-1, -2, -3]), [-2, -4, -6])
        self.assertEqual(MathsUtil.num_by_arr(-1, [-1, -2, -3]), [1, 2, 3])
        self.assertEqual(MathsUtil.num_by_arr(2.5, [1.5, 2.4, 3.05]), [3.75, 6, 7.625])

    """
        Tests that a number is added by a list correctly
    """
    def test_number_plus_array(self):
        self.assertEqual(MathsUtil.num_plus_arr(0, [1, 2, 3]), [1, 2, 3])
        self.assertEqual(MathsUtil.num_plus_arr(2, [-1, -2, -3]), [1, 0, -1])
        self.assertEqual(MathsUtil.num_plus_arr(-1, [-1, -2, -3]), [-2, -3, -4])
        self.assertEqual(MathsUtil.num_plus_arr(2.5, [1.5, 2.4, 3.05]), [4, 4.9, 5.55])

    """
        Test that the slope of a line of best fit for a list of x,y values is calculated correctly.
    """
    def test_estimate_slope(self):
        self.assertEqual(MathsUtil.estimate_slope([1, 2, 3], [1, 2, 3]), 1)

    """
        Test that the y_intercept of a line of best fit for a list of x,y values is calculated correctly with a given slope.
    """
    def test_estimate_y_intercept(self):
        self.assertEqual(MathsUtil.estimate_y_intercept([1, 2, 3], [1, 2, 3], 1), 0)


if __name__ == '__main__':
    unittest.main()
