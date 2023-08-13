#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print()
        exit()
    for i in matrix:
        for j in i:
            if (i.index(j) == len(i) - 1):
                print("{:d}".format(j))
            else:
                print("{:d}".format(j), end=" ")


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer([[]])
