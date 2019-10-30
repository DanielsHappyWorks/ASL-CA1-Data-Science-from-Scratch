class MathsUtil:

    @staticmethod
    def arr_mean(arr):
        return MathsUtil.arr_sum(arr) / len(arr)

    @staticmethod
    def arr_sum(arr):
        sum = 0
        for item in arr:
            sum += item
        return sum

    @staticmethod
    def arr_by_arr(arr1, arr2):
        new_arr = []
        for i, item in enumerate(arr1):
            new_arr.append(item * arr2[i])
        return new_arr

    @staticmethod
    def num_by_arr(num, arr):
        new_arr = []
        for item in arr:
            new_arr.append(num * item)
        return new_arr

    @staticmethod
    def num_plus_arr(num, arr):
        new_arr = []
        for item in arr:
            new_arr.append(num + item)
        return new_arr

    @staticmethod
    def estimate_y_intercept(x, y):
        length_x = len(x)
        mean_x = MathsUtil.arr_mean(x)
        mean_y = MathsUtil.arr_mean(y)

        sum_cross_deviations_y_x = MathsUtil.arr_sum(MathsUtil.arr_by_arr(y, x)) - length_x * mean_y * mean_x
        sum_squared_deviations_x = MathsUtil.arr_sum(MathsUtil.arr_by_arr(x, x)) - length_x * mean_x * mean_x

        return sum_cross_deviations_y_x / sum_squared_deviations_x

    @staticmethod
    def estimate_slope(x, y, y_intercept):
        mean_x = MathsUtil.arr_mean(x)
        mean_y = MathsUtil.arr_mean(y)

        return mean_y - (y_intercept * mean_x)

