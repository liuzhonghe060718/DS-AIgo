def check(matrix, x0, y0, num):
    if num in matrix[x0]:
        return False
    for i in range(9):
        if matrix[i][y0] == num:
            return False
    for i in range(x0 // 2, x0 // 2 + 3):
        for j in range(y0 // 2, y0 // 2 + 3):
            if matrix[i][j] == num:
                return False
    return True

board=[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
def backtrack():
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':  # 找到一个空白格
                for num in range(1, 10):
                    if check(board, i, j, str(num)):
                        board[i][j] = str(num)
                        if backtrack():
                            return board  # 递归求解成功
                        board[i][j] = '.'  # 回溯
                return False  # 所有数字都尝试过了，回溯
    return board # 所有空格都填满了



print(backtrack())


def check(matrix, x0, y0, num):
    if num in matrix[x0]:
        return False
    for i in range(9):
        if matrix[i][y0] == num:
            return False
    for i in range(x0 // 2, x0 // 2 + 3):
        for j in range(y0 // 2, y0 // 2 + 3):
            if matrix[i][j] == num:
                return False
    return True


def backtrack():
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':  # 找到一个空白格
                for num in range(1, 10):
                    if check(board, i, j, str(num)):
                        board[i][j] = str(num)
                        if backtrack():
                            return True  # 递归求解成功
                        board[i][j] = '.'  # 回溯
                return False  # 所有数字都尝试过了，回溯
    return True  # 所有空格都填满了


backtrack()



def solve_sudoku(board):
    def is_valid(board, row, col, num):
        """ 检查 num 放在 board[row][col] 是否有效 """
        block_row, block_col = (row // 3) * 3, (col // 3) * 3
        num = str(num)

        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
            if board[block_row + i // 3][block_col + i % 3] == num:
                return False
        return True

    def backtrack():
        """ 递归回溯求解数独 """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':  # 找到一个空白格
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = str(num)
                            if backtrack():
                                return True  # 递归求解成功
                            board[i][j] = '.'  # 回溯
                    return False  # 所有数字都尝试过了，回溯
        return True  # 所有空格都填满了

    backtrack()


# 示例输入：9x9数独（未解）
sudoku_board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

solve_sudoku(sudoku_board)

# 输出解
for row in sudoku_board:
    print(" ".join(row))