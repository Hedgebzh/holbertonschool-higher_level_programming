#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for i in range(len(matrix)):
        new_sub_list = []
        for idx in range(len(matrix[i])):
            new_sub_list.append(matrix[i][idx] ** 2)
        new_list.append(new_sub_list)
    return (new_list)
