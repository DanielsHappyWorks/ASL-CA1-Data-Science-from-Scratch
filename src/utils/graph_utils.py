import matplotlib.pyplot as graph
import src.constant as constant
from src.utils.maths_util import MathsUtil
import numpy as np
from scipy.stats import norm



class GraphUtils:
    """
        displays a linear regression graph on screen
        :param data
            dictionary containing data to plot as scatter
        :param x_axis
            label to retrieve the x axis values from the dictionary
        :param y_axis
            label to retrieve the y axis values from the dictionary
        :param predicted_y
            list of y values to plot the line against data[x_axis]
    """
    @staticmethod
    def show_linear_regression_graph(data, x_axis, y_axis, predicted_y):
        graph.clf()
        GraphUtils.draw_linear_regression_graph(data, x_axis, y_axis, predicted_y)
        graph.show()

    """
        displays a linear regression graph on screen
        :param column
            array of values to be plotted on the histogram
        :param mean
            mean of the values used in heading and for plot of distribution line
        :param variance
            variance of the values used in heading and for plot of distribution line
        :param standard_deviation
            standard_deviation of the values used in heading and for plot of distribution line
    """
    @staticmethod
    def show_distribution_graph(column, name, mean, median, mode):
        graph.clf()
        GraphUtils.draw_distribution_graph(column, name, mean, median, mode)
        graph.show()

    """
        exports the linear regression graph to a file
        :param data
            dictionary containing data to plot as scatter
        :param x_axis
            label to retrieve the x axis values from the dictionary
        :param y_axis
            label to retrieve the y axis values from the dictionary
        :param predicted_y
            list of y values to plot the line against data[x_axis]
        :param path
            path for where to output the file, should already exist
    """
    @staticmethod
    def export_linear_regression_graph(data, x_axis, y_axis, predicted_y, path):
        graph.clf()
        GraphUtils.draw_linear_regression_graph(data, x_axis, y_axis, predicted_y)

        try:
            graph.savefig(f"{path}lr_{x_axis}_{y_axis}.png")
        except Exception as ex:
            print(f"Could't save graph to {path}lr_{x_axis}_{y_axis}.png Exception: {ex}")

    """
        exports the distribution graph to a file
        :param values
            array of values to be plotted on the histogram
        :param header
            used to name the file
        :param mean
            mean of the values used in heading and for plot of distribution line
        :param variance
            variance of the values used in heading and for plot of distribution line
        :param standard_deviation
            standard_deviation of the values used in heading and for plot of distribution line
        :param path
            path for where to output the file, should already exist
    """
    @staticmethod
    def export_distribution_graph(values, header, mean, median, mode, path):
        graph.clf()
        GraphUtils.draw_distribution_graph(values, header, mean, median, mode)

        try:
            graph.savefig(f"{path}dist_{header}.png")
        except Exception as ex:
            print(f"Could't save graph to {path}dist_{header}.png Exception: {ex}")

    """
        generic draw function to create the graphs for linear regression
        :param data
            dictionary containing data to plot as scatter
        :param x_axis
            label to retrieve the x axis values from the dictionary
        :param y_axis
            label to retrieve the y axis values from the dictionary
        :param predicted_y
            list of y values to plot the line against data[x_axis]
    """
    @staticmethod
    def draw_linear_regression_graph(data, x_axis, y_axis, predicted_y):
        graph.scatter(data[x_axis], data[y_axis], color=constant.SCATTER_COLOUR, marker=constant.SCATTER_MARKER,
                      s=constant.SCATTER_SIZE, label=constant.SCATTER_LABEL, alpha=constant.SCATTER_ALPHA)
        graph.plot(data[x_axis], predicted_y, color=constant.PLOT_COLOUR, label=constant.PLOT_LABEL)
        graph.xlabel(x_axis)
        graph.ylabel(y_axis)
        graph.title(f"{x_axis} vs {y_axis}")
        graph.legend()

    """
        generic draw function to create the graphs for distribution
        :param column
            array of values to be plotted on the histogram
        :param mean
            mean of the values used in heading and for plot of distribution line
        :param variance
            variance of the values used in heading and for plot of distribution line
        :param standard_deviation
            standard_deviation of the values used in heading and for plot of distribution line
    """
    @staticmethod
    def draw_distribution_graph(column, name, mean, median, mode):
        column.sort()
        graph.hist(column, bins=100, density=True, alpha=constant.SCATTER_ALPHA, color=constant.SCATTER_COLOUR)
        x = np.linspace(graph.xlim()[0], graph.xlim()[1], 100)
        graph.xlabel(name)

        # distributions
        p = norm.pdf(x, mean, MathsUtil.arr_standard_deviation(column, mean))
        graph.plot(x, p, color=constant.DISTRIBUTION_MEAN_COLOUR)
        p = norm.pdf(x, median, MathsUtil.arr_standard_deviation(column, median))
        graph.plot(x, p, color=constant.DISTRIBUTION_MEDIAN_COLOUR)
        p = norm.pdf(x, mode, MathsUtil.arr_standard_deviation(column, mode))
        graph.plot(x, p, color=constant.DISTRIBUTION_MODE_COLOUR)

        # averages
        graph.axvline(mean, color=constant.DISTRIBUTION_MEAN_COLOUR,
                      linestyle=constant.DISTRIBUTION_MEAN_LINE_STYLE)
        graph.axvline(median, color=constant.DISTRIBUTION_MEDIAN_COLOUR,
                      linestyle=constant.DISTRIBUTION_MEDIAN_LINE_STYLE)
        graph.axvline(mode, color=constant.DISTRIBUTION_MODE_COLOUR,
                      linestyle=constant.DISTRIBUTION_MODE_LINE_STYLE)

        # title
        graph.legend({"Mean": mean, "Median": median, "Mode": mode})
        mean_title = f"mean={mean:.2f}, variance={MathsUtil.arr_variance(column, mean):.2f} std={MathsUtil.arr_standard_deviation(column, mean):.2f}"
        median_title = f"median={median:.2f}, variance={MathsUtil.arr_variance(column, median):.2f} std={MathsUtil.arr_standard_deviation(column, median):.2f}"
        mode_title = f"mode={mode:.2f}, variance={MathsUtil.arr_variance(column, mode):.2f} std={MathsUtil.arr_standard_deviation(column, mode):.2f}"
        graph.title(f"Distribution: {mean_title}\n{median_title}\n{mode_title}")
