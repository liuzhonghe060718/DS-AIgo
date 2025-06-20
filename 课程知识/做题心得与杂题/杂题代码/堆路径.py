from collections import deque
class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
n=int(input())
nums=list(map(int,input().split()))
root=Treenode(nums[0])
queue=deque([root])
i=1
while i<len(nums) and queue:
    node=Treenode(nums[i])
    if queue[0].left:
        if queue[0].right:
            queue.popleft()
            continue
        else:
            queue[0].right=node
    else:
        queue[0].left=node
    i+=1
    queue.append(node)
ans=[]
big=True
small=True
def dfs(node0,path):
    global big,small
    if node0 is None:
        return
    if node0.left is None and node0.right is None:
        ans.append(' '.join(map(str,path+[node0.val])))
        return
    if node0.left:
        if node0.left.val<node0.val:
            small=False
        else:
            big=False
    if node0.right:
        if node0.right.val<node0.val:
            small=False
        else:
            big=False
    dfs(node0.right,path+[node0.val])
    dfs(node0.left,path+[node0.val])
dfs(root,[])
for j in ans:
    print(j)
if big:
    print('Max Heap')
elif small:
    print('Min Heap')
else:
    print('Not Heap')
