# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:14:36 2019

@author: Daniel
"""

print("Open CSV test.csv")

csv_data = open('test.csv')
headers = csv_data.readline().split(",")
data = dict()
for line in csv_data:
    fields = line.split(",")
    entry = {}
    for i,value in enumerate(fields):
        data.setdefault(headers[i].strip(),[]).append(value.strip())
        
print("print csv as dict")
print(data)