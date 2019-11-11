import matplotlib.pyplot as pyplot
import src.constant as constant


class GraphUtils:
    """
        displays a graph on screen
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
    def show_graph(data, x_axis, y_axis, predicted_y):
        pyplot.clf()
        GraphUtils.draw_graph(data, x_axis, y_axis, predicted_y)
        pyplot.show()

    """
        exports the graph to a file
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
    def export_graph(data, x_axis, y_axis, predicted_y, path):
        pyplot.clf()
        GraphUtils.draw_graph(data, x_axis, y_axis, predicted_y)

        try:
            pyplot.savefig(f"{path}{x_axis}_{y_axis}.png")
        except Exception as ex:
            print(f"Could't save graph to {path}{x_axis}_{y_axis}.png Exception: {ex}")

    """
        generic draw function to create the graphs
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
    def draw_graph(data, x_axis, y_axis, predicted_y):
        pyplot.scatter(data[x_axis], data[y_axis], color=constant.SCATTER_COLOUR, marker=constant.SCATTER_MARKER,
                       s=constant.SCATTER_SIZE, label=constant.SCATTER_LABEL, alpha=constant.SCATTER_ALPHA)
        pyplot.plot(data[x_axis], predicted_y, color=constant.PLOT_COLOUR, label=constant.PLOT_LABEL)
        pyplot.xlabel(x_axis)
        pyplot.ylabel(y_axis)
        pyplot.title(f"{x_axis} vs {y_axis}")
        pyplot.legend()
