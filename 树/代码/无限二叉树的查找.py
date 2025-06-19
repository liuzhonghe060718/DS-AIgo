def count_moves(i, j):
    left_moves = 0
    right_moves = 0

    while i != 1 and j != 1:  # 终止条件: (1,1)
        if i > j:
            left_moves += i // j  # 计算可以跳跃多少次
            i %= j  # 直接更新 i，减少迭代次数
            if i == 0:  # 避免 ZeroDivisionError
                i = 1
        else:
            right_moves += j // i  # 计算可以跳跃多少次
            j %= i  # 直接更新 j，减少迭代次数
            if j == 0:  # 避免 ZeroDivisionError
                j = 1

    # 可能 i != 1 或 j != 1，需要再补一次
    if i > 1:
        left_moves += i - 1
    elif j > 1:
        right_moves += j - 1

    return left_moves, right_moves


n = int(input())  # 读取测试用例数量
for case_num in range(1, n + 1):
    i, j = map(int, input().split())  # 读取 i, j
    left, right = count_moves(i, j)

    # 输出格式
    print(f"Scenario #{case_num}:")
    print(left, right)
    if case_num != n:
        print()  # 题目要求每个案例后面空行
