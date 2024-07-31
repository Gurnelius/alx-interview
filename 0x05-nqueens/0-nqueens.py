#!/usr/bin/python3
'''
The module solves the N queens problem
'''
import sys


def print_solution(board):
    """
    Given a board represented as a 2D list of integers,
    this function finds all the positions of the queens
    on the board and returns them as a list of lists.
    Each inner list contains the row and column indices of a queen.
    The function does not modify the board.

    Parameters:
    - board (List[List[int]]): A 2D list representing the board.
    Each element of the list is an integer representing the presence
    of a queen (1) or absence (0) in a particular position.

    Returns:
    - solution (List[List[int]]): A list of lists representing the
    positions of the queens on the board. Each inner list contains the
    row and column indices of a queen.

    Example:
    >>> board = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    >>> print_solution(board)
    [[1, 1]]
    """

    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_safe(board, row, col):
    '''
    Check if is safe to place a
    queen at board[row][col]
    '''
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col):
    '''
    Utility to solve nqueens
    '''
    if col >= len(board):
        print_solution(board)
        return True

    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens_util(board, col + 1) or res
            board[i][col] = 0  # Backtrack

    return res


def solve_nqueens(n):
    '''
    Solves the n queens problem
    '''
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueens_util(board, 0):
        print("Solution does not exist")
        return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
