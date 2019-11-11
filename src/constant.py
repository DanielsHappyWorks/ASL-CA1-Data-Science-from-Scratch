# main.py
MENU_SELECT_DATA_SET = ['Linear Regression Program:',
                              '1) process build in data set',
                              '2) load in data set',
                              '3) Quit']
MENU_SELECT_DATA_SET_INPUT = "Please select an option (1-3):"
DEFAULT_DATA_SET_FILE = "./input/hour.csv"
DEFAULT_DATA_SET_DATA_TYPES = ['int', 'str', 'int', 'int', 'int', 'int', 'int', 'int', 'int',
                               'int', 'float', 'float', 'float', 'float', 'int', 'int', 'int']
MENU_USE_DATA_SET = ['1) print data set', '2) print header details',
                     '3) run linear regression on data set and print predicted y values',
                     '4) run linear regression on data set and export output',
                     '5) run linear regression on data set and plot output',
                     '6) run linear regression on all columns and export (takes time)', '7) Back:']
MENU_USE_DATA_SET_INPUT = "Please select an option (1-7):"
ENTER_PATH = "Please enter the path to the file:"
ENTER_DELIMITER = "Please enter the delimiter to split the file i.e ',':"
ARE_ALL_INTEGERS = "Are all of the columns integer values? (y/n)"
INVALID_YES_NO = "please enter a valid input! (y, yes, n, no)"
GET_AXIS_X = "Please select the column (integer) for the x axis:"
GET_AXIS_Y = "Please select the column (integer) for the y axis:"

# text_utils.py
CHECK_YES = ["y", "yes"]
CHECK_NO = ["n", "no"]
CHECK_INT = ["i", "int", "integer"]
CHECK_STR = ["s", "str", "string"]
CHECK_FLOAT = ["f", "float"]

# graph_utils.py
SCATTER_COLOUR = "#00CED1"
SCATTER_MARKER = "o"
SCATTER_SIZE = 40
SCATTER_LABEL = "points"
SCATTER_ALPHA = 0.2
PLOT_COLOUR = "#9370DB"
PLOT_LABEL = "line"

# DataFrame.py
DATE_FOTMAT = '%d-%m-%Y-%H-%M-%S'
PREDICTION_EXPORT_COL = "Predicted Y"