board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


def is_on(state, i):
    return (state >> i) & 1


# 将一个数的第i位设置为1
def set_on(state, i):
    return state | (1 << i)  # 从 ^ 改为 |，这是正确的设置位的方式


# 检查在(x0, y0)这个位置，放数字idx+1是否符合数独规则
def check(x0, y0, visit, idx):
    for i in range(9):
        # 检查同一行和同一列是否有重复
        if is_on(visit[x0][i], idx) or is_on(visit[i][y0], idx):
            return False
    # 检查同一个3x3的格子是否有重复
    for i in range(3 * (x0 // 3), 3 * (x0 // 3) + 3):
        for j in range(3 * (y0 // 3), 3 * (y0 // 3) + 3):
            if is_on(visit[i][j], idx):
                return False
    return True


# 初始化visited数组和unfilled列表
visited = [[0] * 9 for i in range(9)]  # visited[i][j]用一个9位的二进制数来表示第i行第j列已经有哪些数字了
unfilled = []  # unfilled列表存储所有需要填写的空格的坐标
for i in range(9):
    for j in range(9):
        if board[i][j] != '.':
            visited[i][j] = set_on(visited[i][j], int(board[i][j]) - 1)  # 如果这个格子有数字，就把对应的位置1
        else:
            unfilled.append((i, j))  # 如果是空格，就加入unfilled列表


# 回溯法解决数独问题
def backtrack(visit, unfill, grad):
    if not unfill:
        return grad  # 如果unfill列表为空，说明所有格子都填完了，返回结果
    xm, ym = unfill.pop()
    # 取出一个空格的坐标
    for num in range(9):  # 尝试填入1到9这9个数字
        if check(xm, ym, visit, num):  # 如果填入的数字符合规则
            new_grad = [row[:] for row in grad]  # 创建一个新的grad，避免修改原来的grad
            new_grad[xm][ym] = str(num + 1)  # 填入数字
            new_visit = [row[:] for row in visit]  # 创建一个新的visit，避免修改原来的visit
            new_visit[xm][ym] = set_on(new_visit[xm][ym], num)
            ans = backtrack(new_visit, list(unfill), new_grad)  # 递归调用backtrack
            if ans:
                return ans  # 如果找到了解，就返回
    unfill.append((xm, ym))  # 如果1到9都不行，就把这个空格放回去，回溯
    return None  # 表示没有找到解


# 调用backtrack函数解决数独问题


# 调用backtrack函数解决数独问题
solved_board = backtrack(visited, unfilled, board)

# 打印结果
if solved_board:
    for row in solved_board:
        print(row)
else:
    print("No solution found.")  # 如果没有找到解，就打印"No solution found."
