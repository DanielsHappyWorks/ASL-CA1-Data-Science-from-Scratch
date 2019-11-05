import matplotlib.pyplot as pyplot


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
        pyplot.savefig(f"{path}{x_axis}_{y_axis}.png")

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
        pyplot.scatter(data[x_axis], data[y_axis], color="#00CED1",
                       marker="o", s=40, label='points', alpha=0.2)
        pyplot.plot(data[x_axis], predicted_y, color="#9370DB", label='line')
        pyplot.xlabel(x_axis)
        pyplot.ylabel(y_axis)
        pyplot.title(f"{x_axis} vs {y_axis}")
        pyplot.legend()
