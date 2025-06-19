#16:20
class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

import sys

# 一次性读取所有行，返回一个列表
lines = sys.stdin.readlines()
for x in range(len(lines)):
    for y in range(len(lines[x].strip())):
        print(lines[x][y])

import sys

# 一次性读取所有行，返回一个列表
lines = sys.stdin.readlines()
print("你输入的行数是：", len(lines))
print("内容如下：")
for line in lines:
    print(line.strip())  # strip() 去掉每行的换行符
