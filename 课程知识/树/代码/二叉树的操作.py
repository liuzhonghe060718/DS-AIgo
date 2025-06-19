class Treenode:
    def __init__(self, val):
        self.val = val
        self.children = [None, None]  # [left, right]
        self.parent = None  # 父节点


def find_parent_and_dir(node):
    if node.parent is None:
        return None, None  # 根节点没有父节点
    parent = node.parent
    if parent.children[0] == node:
        return parent, 0  # 左孩子
    elif parent.children[1] == node:
        return parent, 1  # 右孩子
    else:
        raise ValueError("Node is not a child of its parent")


def exchange(node1, node2):
    parent1, dir1 = find_parent_and_dir(node1)
    parent2, dir2 = find_parent_and_dir(node2)

    # 更新父节点的 children
    if parent1 is not None:
        parent1.children[dir1] = node2
    if parent2 is not None:
        parent2.children[dir2] = node1

    # 更新节点的 parent
    node1.parent, node2.parent = node2.parent, node1.parent


def ask(node):
    if node.children[0] is None:
        return node.val
    return ask(node.children[0])


# 主程序
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    tree = {j: Treenode(j) for j in range(n)}
    for _ in range(n):
        father, le, ri = map(int, input().split())
        if le != -1:
            tree[father].children[0] = tree[le]
            tree[le].parent = tree[father]
        if ri != -1:
            tree[father].children[1] = tree[ri]
            tree[ri].parent = tree[father]
    for _ in range(m):
        word = list(map(int, input().split()))
        if word[0] == 1:
            node1 = tree[word[1]]
            node2 = tree[word[2]]
            exchange(node1, node2)
        else:
            node = tree[word[1]]
            print(ask(node))