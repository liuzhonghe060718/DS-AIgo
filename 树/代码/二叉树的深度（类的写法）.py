class Treenode:
    def __init__(self):
        self.left=None
        self.right=None
def tree_depth(node):
    if node is None:
        return 0
    left_depth=tree_depth(node.left)
    right_depth=tree_depth(node.right)
    return max(left_depth,right_depth)+1
def count_leaves(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left)+count_leaves(node.right)
n=int(input())
nodes=[Treenode() for _ in range(n)]
has_parent=[False]*n
for i in range(n):
    left_idx,right_idx=map(int,input().split())
    if left_idx!=-1:
        nodes[i].left=nodes[left_idx]
        has_parent[left_idx]=True
    if right_idx!=-1:
        nodes[i].right=nodes[right_idx]
        has_parent[right_idx]=True
root=nodes[has_parent.index(False)]
height=tree_depth(root)
leaves=count_leaves(root)
print(f'{height-1} {leaves}')