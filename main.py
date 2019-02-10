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
                   'Count.2': 'Count chb', 'Amount.2': "Amount chb", 'Count.3': 'Count repr', 'Amount.3': "Amount repr",
                   'Count.4': 'Count Declines' }, inplace=True)


'''choose columns for delete'''


columns = ['Amount.4', 'Count.5', 'Amount.5', 'Count.6', 'Amount.6', 'Count.7', 'Amount.7']
df = df.drop(columns, axis=1)


'''create dict with companies names and currency'''


def data_dict(my_dict):
    my_dict = {}
    keys = df['Merchant Name']
    values = df['Currency']

    for k, v in my_dict.items():
         keys.append(k)
         values.append(v)




