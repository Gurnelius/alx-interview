#!/usr/bin/python3

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the
    Pascal’s triangle of size n
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        # Start each row with 1
        row = [1]
        # Generate the middle elements of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End each row with 1
        row.append(1)
        triangle.append(row)

    return triangle
