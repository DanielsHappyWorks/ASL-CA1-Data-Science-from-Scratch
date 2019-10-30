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

