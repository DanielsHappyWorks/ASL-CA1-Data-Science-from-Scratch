import matplotlib.pyplot as graph
import src.constant as constant
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
    def show_distribution_graph(column, mean, variance, standard_deviation):
        print(column)
        graph.clf()
        GraphUtils.show_distribution_graph(column, mean, variance, standard_deviation)
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
        :param column
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
    def export_distribution_graph(column, header, mean, variance, standard_deviation, path):
        graph.clf()
        GraphUtils.draw_distribution_graph(column, mean, variance, standard_deviation)

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
    def draw_distribution_graph(column, mean, variance, standard_deviation):
        column.sort()
        graph.hist(column, bins=100, density=True, alpha=constant.SCATTER_ALPHA, color=constant.SCATTER_COLOUR)
        x = np.linspace(graph.xlim()[0], graph.xlim()[1], 100)
        p = norm.pdf(x, mean, standard_deviation)
        graph.plot(x, p, linewidth=2, color=constant.PLOT_COLOUR)
        graph.title(f"Distribution: mean={mean:.2f}, var={variance:.2f} std={standard_deviation:.2f}")
