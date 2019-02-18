str = 'human'
h_letters = []
for letter in str:
    h_letters.append(letter)

print(h_letters)

h_lett = [letter for letter in str]
print(h_lett)
# https://www.programiz.com/python-programming/list-comprehension#lcvf

lettrs1 = list(map(lambda x: x, 'human'))
print(lettrs1)

num_list = [x for x in range(20) if x%2 ==0]
print(num_list)
num_list1 = [x for x in range(100) if x%2 ==0 if x%5 == 0]
print(num_list1)

obj = ['even' if i%2 ==0 else 'odd' for i in range(10)]
print(obj)
# Suppose, we need to compute transpose of a matrix which requires nested for loop.
# Let’s see how it is done using normal for loop first.

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
transposed = [[row[i] for row in matrix] for i in range(4)]
# for i in range(len(matrix[0])):
#     transposed_row = []
#
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)


print(transposed) #[[1, 4], [2, 5], [3, 6], [4, 8]]
matrix1 = [[1, 4], [2, 5], [3, 6], [4, 8]]
transpose = [[row[i] for row in matrix1] for i in range(2)]
print(transpose)