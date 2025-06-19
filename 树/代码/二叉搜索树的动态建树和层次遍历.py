from collections import deque



class Treenode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val

nums=list(map(int,input().split()))
def build_tree(value,node):
    if value==node.val:
        return
    if value<node.val:
        if node.left is None:
            node.left=Treenode(value)
            return
        else:
            build_tree(value,node.left)
    else:
        if node.right is None:
            node.right=Treenode(value)
            return
        else:
            build_tree(value,node.right)
root=Treenode(nums[0])
n=len(nums)
for i in range(1,n):
    build_tree(nums[i],root)
def level_order(node):
    result=[]
    queue=deque([node])
    while queue:
        nodes=queue.popleft()
        result.append(str(nodes.val))
        if nodes.left is not None:
            queue.append(nodes.left)
        if nodes.right is not None:
            queue.append(nodes.right)
    return ' '.join(result)
print(level_order(root))







