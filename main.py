import os
import pandas as pd
import numpy as np


'''
The handler of a files in the CSV format.
Calculation set uped by finance department.
Output: three column csv file included company's name/currencies/counted income
'''

file = pd.read_csv('/home/julia/Downloads/summary.csv')

df = pd.DataFrame(file)
df.columns.get_level_values(0)

'''find all column names and rename them'''

print(df.keys())
print (df.columns)

df.rename(columns={'Count': 'Count sales', 'Amount': 'Amount sales', 'Count.1': 'Count refunds', 'Amount.1': 'Amount refunds',
                   'Count.2': 'Count chb', 'Amount.2': "Amount chb" }, inplace=True)



print(df.dtypes)
