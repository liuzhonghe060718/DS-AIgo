

class Treenode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
    def __str__(self):
        return self.val
n=int(input())

def build_tree(inorder,preorder):
    if len(inorder)==0 or len(preorder)==0:
        return None
    word=preorder.pop(0)
    node=Treenode(word)
    idx=inorder.index(word)
    node.left = build_tree(inorder[:idx], preorder)
    node.right=build_tree(inorder[idx+1:],preorder)
    return node

preorder=list(map(int,input().split()))
inorder=sorted(preorder)
root=build_tree(inorder,preorder)
ans=[]
def last_order(node):
    if node.left is not None:
        last_order(node.left)
    if node.right is not None:
        last_order(node.right)
    ans.append(node.val)

last_order(root)
print(' '.join(map(str,ans)))


n=int(input())
preorder=list(map(int,input().split()))


def build_tree(s):
    if len(s)==0:
        return
    node=Treenode(s[0])
    idx=len(s)
    for i in range(1,len(s)):
        if s[i]>s[0]:
            idx=i
            break
    node.left=build_tree(s[1:idx])
    node.right=build_tree(s[idx:])
    return node
root=build_tree(preorder)
ans=[]
def last_order(node):
    if node.left is not None:
        last_order(node.left)
    if node.right is not None:
        last_order(node.right)
    ans.append(node.val)

last_order(root)
print(' '.join(map(str,ans)))

