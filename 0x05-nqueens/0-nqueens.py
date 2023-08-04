import sys

def is_safe(board, row, col, N):
    # Check if the current position is safe for the queen
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check for queens in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check for queens in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_helper(board, 0, N, solutions)
    return solutions

def solve_nqueens_helper(board, row, N, solutions):
    if row == N:
        # Found a solution, add it to the list of solutions
        solutions.append([''.join(row) for row in board])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            # Place a queen at the current position
            board[row][col] = 'Q'

            # Recursively solve for the next row
            solve_nqueens_helper(board, row + 1, N, solutions)

            # Backtrack and remove the queen from the current position
            board[row][col] = '.'

def main():
    # Check the command line arguments
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

    solutions = solve_nqueens(N)

    # Print the solutions
    for solution in solutions:
        print('\n'.join(solution))
        print()

if __name__ == '__main__':
    main(
