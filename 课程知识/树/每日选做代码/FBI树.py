n=int(input())
s0=input()
class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def build_tree(s):
    if len(s)==1:
        if s=='1':
            return Treenode('I')
        else:
            return Treenode('B')
    left=build_tree(s[:len(s)//2])
    right=build_tree(s[len(s)//2:])
    if left.val!=right.val:
        node=Treenode('F')
    else:
        node=Treenode(left.val)
    node.left=left
    node.right=right
    return node
ans=[]
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    ans.append(node.val)
root=build_tree(s0)
postorder(root)
print(''.join(ans))