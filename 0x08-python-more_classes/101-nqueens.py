import sys

def is_safe(board, row, col):
    # Check the column on top for queens
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper-left diagonal for queens
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal for queens
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def solve(board, row):
        if row == n:
            for r in board:
                print([i, r.index(1)] for i in range(n))
            print()
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)
