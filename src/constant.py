# main.py
MENU_SELECT_DATA_SET = ['Linear Regression Program:',
                              '1) process build in data set',
                              '2) load in data set',
                              '3) Quit']
MENU_SELECT_DATA_SET_INPUT = "Please select an option (1-3):"
DEFAULT_DATA_SET_FILE = "./input/hour.csv"
DEFAULT_DATA_SET_DATA_TYPES = ['int', 'str', 'int', 'int', 'int', 'int', 'int', 'int', 'int',
                               'int', 'float', 'float', 'float', 'float', 'int', 'int', 'int']
MENU_USE_DATA_SET = ['1) print data set',
                     '2) print header details',
                     '3) print mean, variance, and standard deviation for 1 column',
                     '4) plot normal distribution on 1 column',
                     '5) export normal distribution on 1 column',
                     '6) export all normal distribution graphs and calculations',
                     '7) run linear regression on 2 columns and print predicted y values',
                     '8) run linear regression on 2 columns and export output',
                     '9) run linear regression on 2 columns and plot output',
                     '10) run linear regression on all columns and export (takes time)',
                     '11) Back:']
MENU_USE_DATA_SET_INPUT = "Please select an option (1-7):"
ENTER_PATH = "Please enter the path to the file:"
ENTER_DELIMITER = "Please enter the delimiter to split the file i.e ',':"
ARE_ALL_INTEGERS = "Are all of the columns integer values? (y/n)"
INVALID_YES_NO = "please enter a valid input! (y, yes, n, no)"
GET_COLUMN = "Please select the column (integer/float):"
GET_AXIS_X = "Please select the column (integer/float) for the x axis:"
GET_AXIS_Y = "Please select the column (integer/float) for the y axis:"

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

# data_frame.py
DATE_FOTMAT = '%d-%m-%Y-%H-%M-%S'
PREDICTION_EXPORT_COL = "Predicted Y"