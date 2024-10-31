#acccessing items in a matrix

def sum_of_row(my_matrix, row_no: int):
    #choose the desired row from withinthe matrix
    row = my_matrix[row_no]
    row_sum = 0
    for item in row:
        row_sum += item
    return row_sum
    
m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_row(m, 2)

print(my_sum)

def sum_of_column(my_matrix, column_no: int):
    #go through each row and select the item at the chosen position
    column_sum = 0
    for row in my_matrix:
        column_sum += row[column_no]
    return column_sum

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_column(m, 2)

print(my_sum)


def change_value(my_matrix, row_no: int, column_no: int, new_value: int):
    #choose the desired row
    row = my_matrix[row_no]
    row[column_no] = new_value

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]  

print(m)
change_value(m, 2, 3, 1000)
print(m)

for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j] += 1000
print(m)
