import os
import pandas as pd
import numpy as np


'''
The handler of a files in the CSV format.
Calculation set uped by finance department.
Output: three column csv file included company's name/currencies/counted income
'''

file = pd.read_csv('/home/julia/Downloads/summary.csv')
print(file.head())