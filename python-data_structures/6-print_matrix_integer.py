#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for idx in range(len(matrix[i])):
            print("{:d}".format(matrix[i][idx]), end="")
            if idx != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")

