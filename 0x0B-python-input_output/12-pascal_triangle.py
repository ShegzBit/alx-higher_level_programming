#!/usr/bin/python3
"""
Pascal triangle
Technical Interview prep
"""


def pascal_triangle(n):
    """
    Pascal triangle
    """
    default = [[1], [1, 1]]
    if n <= 0:
        return []
    if n - 1 < len(default):
        return default[:n]
    triangle = default[:]
    # looping through the outer list
    for i in range(1, n - 1):
        j = 0
        new_row = []
        new_row.append(1)
        # looping through each inner list to use value
        # for generation of new list
        while j < len(triangle[i]) - 1:
            prev = triangle[i][j]
            if j + 1 < len(triangle[i]):
                # adding current value to next row
                cur = prev + triangle[i][j + 1]
            new_row.append(cur)
            j += 1
        new_row.append(1)
        # adding new pascal row to the main triangle
        triangle.append(new_row)
    return triangle


if __name__ == "__main__":
    print(pascal_triangle(-2))
    print(pascal_triangle(0))
    print(pascal_triangle(1))
    print(pascal_triangle(2))
    print(pascal_triangle(3))
    print(pascal_triangle(4))
