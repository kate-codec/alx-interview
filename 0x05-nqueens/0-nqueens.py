import sys

def is_attacked(board, row, col):
  for i in range(row):
    if board[i][col] == 1:
      return True

  for i in range(row, n):
    for j in range(col):
      if board[i][j] == 1 and (i - row) == (j - col) or (i - row) == (col - j):
        return True

  for i in range(row - 1, -1, -1):
    for j in range(col - 1, -1, -1):
      if board[i][j] == 1 and (row - i) == (col - j) or (row - i) == (j - col):
        return True

  return False

def nqueens(board, row):
  if row == n:
    print(board)
    return

  for col in range(n):
    if not is_attacked(board, row, col):
      board[row][col] = 1
      nqueens(board, row + 1)
      board[row][col] = 0

def main():
  if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number")
    exit(1)

  if n < 4:
    print("N must be at least 4")
    exit(1)

  board = [[0 for i in range(n)] for j in range(n)]
  nqueens(board, 0)

if __name__ == "__main__":
  main()
