def solution():
    def updateMatrix(matrix):
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[0] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0 :
                    dist[i][j] = max(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = max(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向左移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist
    print(updateMatrix())
