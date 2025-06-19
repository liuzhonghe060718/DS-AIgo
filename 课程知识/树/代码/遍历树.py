#13:16
class Treenode:
    def __init__(self,val):
        self.val=val
        self.children=[]
    def __lt__(self, other):
        return self.val<other.val
n=int(input())
tree={}
not_root=set()
for i in range(n):
    nums=list(map(int,input().split()))
    if nums[0] in tree:
        node=tree[nums[0]]
    else:
        node=Treenode(nums[0])
        tree[nums[0]]=node
    for num in nums[1:]:
        if num in tree:
            node.children.append(tree[num])
        else:
            node1=Treenode(num)
            node.children.append(node1)
            tree[num]=node1
        not_root.add(num)
ans=[]
for x in set(tree.keys())-not_root:
    root=x
root=tree[root]
stack=[root]
visited=set()
while stack:
    nodes=stack.pop()
    if nodes in visited:
        print(nodes.val)
        continue
    visited.add(nodes)
    for node0 in sorted(nodes.children+[nodes],reverse=True):
        stack.append(node0)






