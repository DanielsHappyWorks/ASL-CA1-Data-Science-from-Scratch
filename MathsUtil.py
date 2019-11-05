class MathsUtil:
    """
        gets the mean average of a list
        :param arr
            array of integer/float values used to get the mean average
        :returns float
            the average of all values in the list
    """
    @staticmethod
    def arr_mean(arr):
        return MathsUtil.arr_sum(arr) / len(arr)

    """
        gets the sun of all the values in a list
        :param arr
            array of integer/float values used to get the sum
        :returns float/int
            the sum of all values in the list
    """
    @staticmethod
    def arr_sum(arr):
        sum = 0
        for item in arr:
            sum += item
        return sum

    """
        multiplies one array by another assuming they are the same size
        :param arr1
            first list for multiplication
        :param arr2
            second list for multiplication
        :return
            returns new list with the multiplied values
    """
    @staticmethod
    def arr_by_arr(arr1, arr2):
        new_arr = []
        for i, item in enumerate(arr1):
            new_arr.append(item * arr2[i])
        return new_arr

    """
        multiplies a number by a list
        :param num
            number used for multiplication
        :param arr
            list to be multiplied by the number
        :return
            returns new list with the multiplied value
    """
    @staticmethod
    def num_by_arr(num, arr):
        new_arr = []
        for item in arr:
            new_arr.append(num * item)
        return new_arr

    """
        adds a number to a list
        :param num
            number used for adding
        :param arr
            list to be added to
        :return
            returns new list with the added value
    """
    @staticmethod
    def num_plus_arr(num, arr):
        new_arr = []
        for item in arr:
            new_arr.append(num + item)
        return new_arr

    """
        estimates the y intercept based on 2 arrays of the same size for Linear Regression (lr)
        :param x
            list of x values to calculate lr y intercept
        :param y
            list of y values to calculate lr y intercept
        :return
            returns the y intercept of a line for lr
    """
    @staticmethod
    def estimate_y_intercept(x, y):
        length_x = len(x)
        mean_x = MathsUtil.arr_mean(x)
        mean_y = MathsUtil.arr_mean(y)

        sum_cross_deviations_y_x = MathsUtil.arr_sum(MathsUtil.arr_by_arr(y, x)) - length_x * mean_y * mean_x
        sum_squared_deviations_x = MathsUtil.arr_sum(MathsUtil.arr_by_arr(x, x)) - length_x * mean_x * mean_x

        return sum_cross_deviations_y_x / sum_squared_deviations_x

    """
        estimates the slope based on 2 arrays (same size) and y intercept for Linear Regression (lr)
        :param x
            list of x values
        :param y
            list of y values
        :param y_intercept
            int/float value used to calculate slope
        :return
            returns the slope of a line for lr
    """
    @staticmethod
    def estimate_slope(x, y, y_intercept):
        mean_x = MathsUtil.arr_mean(x)
        mean_y = MathsUtil.arr_mean(y)

        return mean_y - (y_intercept * mean_x)

