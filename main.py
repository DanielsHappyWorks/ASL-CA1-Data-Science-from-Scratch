from DataFrame import DataFrame

#TO DO
#   Catch invalid inputs for selections
#   catch invalid path
#   check the given path is a csv
#   add linear regression for 2 columns
#   add export for linear regression modal
#   add ability to plot the linear regression line with values
#   remove duplication

def main():
    while True:
        print()
        print("Linear Regression Program:")
        print("1) process build in data set:")
        print("2) load in data set:")
        print("3) Quit:")
        selection = int(input("Please select an option (0-2):"))
        if selection == 1:
            print("Opening CSV ./DataSet/hour.csv")
            data_frame = createDataFrame('./DataSet/hour.csv')
            useDataFrame(data_frame)
        elif selection == 2:
            path = input("Please enter the path to the file:")
            print(f"Opening CSV {path}")
            data_frame = createDataFrame(path)
            useDataFrame(data_frame)
        elif selection == 3:
            break
    
def createDataFrame(path):
    csv_data = open(path)
    headers = csv_data.readline().split(",")
    return DataFrame(headers, csv_data, [], ',')

def useDataFrame(data_frame):
    while True:
        print()
        print("1) print data set:")
        print("2) run linear regression on data set and print output:")
        print("3) run linear regression on data set and plot output:")
        print("4) run linear regression on data set and export output:")
        print("5) Back:")
        selection = int(input("Please select an option (0-2):"))
        if selection == 1:
            data_frame.printData()
        elif selection == 2:
            print()
            data_frame.printHeadings()
            x_axis = int(input("Please select the column (integer) for the x axis:"))
            y_axis = int(input("Please select the column (integer) for the y axis:"))
            data_frame.runLinearRegression(x_axis, y_axis)
            data_frame.printLinearRegressionOutput()
        elif selection == 4:
            print()
            data_frame.printHeadings()
            x_axis = int(input("Please select the column (integer) for the x axis:"))
            y_axis = int(input("Please select the column (integer) for the y axis:"))
            file_name = int(input("Please specify a file directory and name i.e ./export.csv:"))
            data_frame.runLinearRegression(x_axis, y_axis)
            data_frame.exportLinearRegressionOutput(file_name)
        elif selection == 3:
            print()
            data_frame.printHeadings()
            x_axis = int(input("Please select the column (integer) for the x axis:"))
            y_axis = int(input("Please select the column (integer) for the y axis:"))
            file_name = int(input("Please specify a file directory and name i.e ./export.csv:"))
            data_frame.runLinearRegression(x_axis, y_axis)
            data_frame.exportLinearRegressionOutput(file_name)
        elif selection == 5:
            break


main()
