# Sudoku Solver using Backtracking

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try all numbers from 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):  # Recursively try to solve the rest of the board
                            return True
                        board[row][col] = 0  # Backtrack if not valid
                return False  # No valid number found, backtrack
    return True  # Solved

# Sample Sudoku puzzle (0 represents an empty cell)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

if __name__ == "__main__":
    print("Sudoku Puzzle:")
    print_board(sudoku_board)
    
    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku:")
        print_board(sudoku_board)
    else:
        print("No solution exists.")
