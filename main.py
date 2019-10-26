from DataFrame import DataFrame

#TO DO
#   Catch invalid inputs for selections
#   catch invalid path
#   check the given path is a csv
#   add linear regression for 2 columns

def main():
    while True:
        print("Linear Regression Program:")
        print("0) process build in data set:")
        print("1) load in data set:")
        print("2) Quit:")
        selection = int(input("Please select an option (0-2):"))
        if(selection == 0):
            print("Opening CSV ./DataSet/day.csv")
            data_frame = createDataFrame('./DataSet/day.csv')
            useDataFrame(data_frame)
        elif(selection == 1):
            path = input("Please enter the path to the file:")
            print(f"Opening CSV {path}")
            data_frame = createDataFrame(path)
            useDataFrame(data_frame)
        elif(selection == 2):
            break
    
def createDataFrame(path):
    csv_data = open(path)
    headers = csv_data.readline().split(",")
    return DataFrame(headers, csv_data, [], ',')

def useDataFrame(data_frame):
    while True:
        print("0) print data set:")
        print("1) run linear regression on data set:")
        print("2) Back:")
        selection = int(input("Please select an option (0-2):"))
        if(selection == 0):
            data_frame.printData()
        elif(selection == 1):
            data_frame.runLinearRegression()
        elif(selection == 2):
            break

main()
