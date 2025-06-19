

class Treenode:
    def __init__(self, val):
        self.val = val
        self.children = []

s=list(input())
if len(s)==1:
    nodes=Treenode(s[0])
stack=[]
n=len(s)
for i in range(n):
    if s[i]=='(':
        stack.append(now_node)
    elif s[i]==',':
        continue
    elif s[i]==')':
        if stack:
            nodes=stack.pop()
    else:
        now_node=Treenode(s[i])
        if stack:
            stack[-1].children.append(now_node)
ans1=[]
def preorder(node):
    if node is None:
        return
    ans1.append(node.val)
    for node1 in node.children:
        preorder(node1)
ans2=[]
def postorder(node):
    if node is None:
        return

    for node1 in node.children:
        postorder(node1)
    ans2.append(node.val)
postorder(nodes)
preorder(nodes)
print(''.join(ans1))
print(''.join(ans2))
