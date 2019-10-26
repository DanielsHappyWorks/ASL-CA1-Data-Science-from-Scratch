# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:14:36 2019

@author: Daniel
"""

from DataFrame import DataFrame

def main():
    data_frame = createDataFrame()
    
def createDataFrame():
    print("Open CSV test.csv")
    csv_data = open('test.csv')
    headers = csv_data.readline().split(",")
    data_frame = DataFrame(headers, csv_data, [], ',')
    print("print csv as dict")
    print(data_frame.data)

main()
