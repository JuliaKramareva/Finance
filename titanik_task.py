import pandas as pd
import numpy as np
import re

data = pd.read_csv('/home/julia/Desktop/titanic.csv', index_col='PassengerId')

print(data.head())
print(data.dtypes)

'''Какое количество мужчин и женщин ехало на корабле? '''

a1 = pd.DataFrame(data['Sex'])
print(a1['Sex'].value_counts())


'''Какой части пассажиров удалось выжить?'''

a2 = pd.DataFrame(data['Survived'])
print(a2)
Survived = round(int(a2['Survived'][data.Survived >0].value_counts()) / len(a2['Survived']) * 100,2)
print(Survived)

'''Какую долю пассажиры первого класса составляли среди всех пассажиров?'''

a3 = pd.DataFrame(data['Pclass'])
print(a3)
First_class = round(int(a3['Pclass'][a3.Pclass == 1].count()) / len(a3['Pclass']) * 100, 2)

print(First_class)

'''Посчитайте среднее и медиану возраста пассажиров.'''

a4 = pd.DataFrame(data['Age']).dropna(0)
a4_mean = round(a4.mean(), 2)
a4_median = a4.median()
print(a4_mean, a4_median)

'''Коррелируют ли число братьев/сестер с числом родителей/детей?
Посчитайте корреляцию Пирсона между признаками SibSp и Parch.'''

corr = data['SibSp'].corr(data['Parch'])
print(corr)

'''Какое самое популярное женское имя на корабле?'''

# a6 = pd.DataFrame(data['Name'])
# print(a6)
def clean_name(name):
    soname = re.search('^[^,]+, (.*)', name)
    if soname:
        name = soname.group(1)

    soname = re.search('\(([^)]+)\)', name)
    if soname:
        name = soname.group(1)

    name = re.sub('(Miss\. |Mrs\. |Ms\. )', '', name)
    name = name.split(' ')[0].replace('"', '')

    return name

names = data[data['Sex'] == 'female']['Name'].map(clean_name)
name_count = names.value_counts()
print(names, name_count)

