import heapq
n=int(input())
values=list(map(int,input().split()))
class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    def __lt__(self, other):
        return self.val<other.val
tree=[Treenode(value) for value in values]
heapq.heapify(tree)
while len(tree)>1:
    left=heapq.heappop(tree)
    right=heapq.heappop(tree)
    new_node=Treenode(left.val+right.val)
    new_node.left=left
    new_node.right=right
    heapq.heappush(tree,new_node)
ans=0
def cal(node,high):
    global ans
    if node.left is None and node.right is None:
        ans+=node.val*high
    if node.left:
        cal(node.left,high+1)
    if node.right:
        cal(node.right,high+1)
cal(tree[0],0)
print(ans)




