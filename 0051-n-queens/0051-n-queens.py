from typing import List

class Solution:

  def can_place(self, board, row, col, n):

    for i in range(row):
      if board[i][col] == 1:
        return False
      if ((col - (row - i)) >= 0 and  board[i][col - (row - i)] == 1):
        return False
      if (col + (row - i)) < n and board[i][col + (row - i)] == 1:
        return False

    return True
  
  def solvex(self, board, row, n, solutions):

    if row == n:
      solutions.append([cell[:] for cell in board])
      return True

    for cell in range(n):
      if self.can_place(board, row, cell, n):

        board[row][cell] = 1
        if self.solvex(board, row + 1, n, solutions):
          return True

        board[row][cell] = 0
    
    return False

  def solveNQueens(self, n: int) -> List[List[str]]:

    solutions = []
    def solvex(board, row):
      if row == n:
        solutions.append(["".join('Q' if cell == 1 else '.' for cell in row) for row in board])
        return

      for cell in range(n):
        if self.can_place(board, row, cell, n):
          board[row][cell] = 1
          solvex(board, row + 1)
          board[row][cell] = 0

    board = [[0] * n for _ in range(n)]
    solvex(board, 0)

    return solutions