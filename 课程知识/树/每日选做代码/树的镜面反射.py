#15:45
from collections import deque
n=int(input())


class Twonode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.children=[]
    def __repr__(self):
        return f'{ self.val}'
tree=list(input().split())
stack=[]

for x in range(len(tree)):
    value,active=tree[x][0],tree[x][1]
    node=Twonode(value)
    if x==0:
        root=node

    if stack and node:
        i=-1
        if stack[-1]==1:
            i=-2
        if stack[i].left:
            stack[i].right=node
        else:
            stack[i].left=node
    if active=='0':
        stack.append(node)
    else:
        stack.append(1)
    while len(stack)>=3 and stack[-1]==stack[-2]==1:
        for i in range(3):
            stack.pop()
        stack.append(1)
def change(node0):
    if node0 is None or node0.val=='$':
        return
    change(node0.left)
    change(node0.right)
    if node0.left:
        n_node=node0.left
        while n_node and n_node.val!='$':
            node0.children.append(n_node)
            n_node=n_node.right
change(root)
def post_level():
    ans=[]
    result=[]
    queue=deque([root])
    while queue:
        for j in range(len(queue)):
            now_node=queue.popleft()
            result.append(now_node.val)
            for nodem in now_node.children:
                queue.append(nodem)
        ans.extend(result[::-1])
        result.clear()
    return ' '.join(ans)
print(post_level())









