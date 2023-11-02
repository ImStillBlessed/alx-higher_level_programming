#!/usr/bin/python3
import sys
def is_safe(board, row, col):
    # Check the column on top for queens
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print([row, solution.index(row)])
        print()

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def solve(board, row, solutions):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board.append(col)
                solve(board, row + 1, solutions)
                board.pop()

    solutions = []
    solve([], 0, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
