from DataFrame import DataFrame

def main():
    while True:
        print("Linear Regression Program:")
        print("0) process build in data set:")
        print("1) load in data set:")
        print("2) Quit:")
        selection = int(input("Please select an option (0-2):"))
        if(selection == 0):
            print("Open CSV 'DataSet/day.csv'")
            data_frame = createDataFrame('DataSet/day.csv')
            print("print csv as dict")
            data_frame.printData();
        elif(selection == 1):
            path = input("Please enter the path to the file:")
            print(f"Open CSV {path}")
            data_frame = createDataFrame(path)
            print("print csv as dict")
            data_frame.printData();
        elif(selection == 2):
            break
    
def createDataFrame(path):
    csv_data = open(path)
    headers = csv_data.readline().split(",")
    return DataFrame(headers, csv_data, [], ',')

main()
