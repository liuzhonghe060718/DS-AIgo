s=input()
class Treenode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
stack=[]
for char in s:
    if char.isalpha():
        node=Treenode(char)
        if stack:
            if stack[-1]=='.':
                stack[-2].right=node
            else:
                stack[-1].left=node
        stack.append(node)
    else:
        stack.append(char)
    while len(stack)>=2 and stack[-1]==stack[-2]=='.':
        for i in range(3):
            node=stack.pop()
        stack.append('.')
def postorder(nodes):
    ans=[]
    if nodes.left is not None:
        ans.extend(postorder(nodes.left))
    if nodes.right is not None:
        ans.extend(postorder(nodes.right))
    ans.append(nodes.val)
    return ans
def midorder(nodes):
    ans = []
    if nodes.left is not None:
        ans.extend(midorder(nodes.left))
    ans.append(nodes.val)
    if nodes.right is not None:
        ans.extend(midorder(nodes.right))
    return ans
print(''.join(midorder(node)))
print(''.join(postorder(node)))