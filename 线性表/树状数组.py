class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)  # 1-based index

    def update(self, index, delta):
        """在 index 位置加上 delta"""
        while index <= self.n:
            self.bit[index] += delta
            index += index & -index  # LSB，找到下一个需要更新的节点

    def query(self, index):
        """返回前 index 项的前缀和"""
        sum_ = 0
        while index > 0:
            sum_ += self.bit[index]
            index -= index & -index  # LSB，找到前一个影响区间
        return sum_

    def range_query(self, left, right):
        """返回区间 [left, right] 的和"""
        return self.query(right) - self.query(left - 1)

# 示例
arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2]
ft = FenwickTree(len(arr))

# 初始化树状数组
for i, val in enumerate(arr):
    ft.update(i + 1, val)

print(ft.range_query(3, 7))  # 查询索引 3 到 7 的区间和
