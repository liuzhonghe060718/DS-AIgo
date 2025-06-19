n=int(input())
class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def preorder(node0):
    if node0 is None or node0.val=='*':
        return []
    ans=[node0.val]
    ans.extend(preorder(node0.left))
    ans.extend(preorder(node0.right))
    return ans
def inorder(node0):
    ans=[]
    if node0 is None or node0.val =='*':
        return ans
    ans.extend(inorder(node0.left))
    ans.append(node0.val)
    ans.extend(inorder(node0.right))
    return ans
def postorder(node0):
    ans=[]
    if node0 is None or node0.val =='*':
        return ans
    ans.extend(postorder(node0.left))
    ans.extend(postorder(node0.right))
    ans.append(node0.val)
    return ans
for i in range(n):
    tree={}
    while True:
        word=input().split('-')
        if word[0]=='0':
            break
        level,value=len(word),word[-1]

        node=Treenode(value)
        if level==1:
            root=node
        if value !='*':
            if level not in tree:
                tree[level]=[node]
            else:
                tree[level].append(node)
        if level-1 in tree:
            if tree[level-1][-1].left:
                tree[level-1].pop().right=node
            else:
                tree[level-1][-1].left=node
    print(''.join(preorder(root)))
    print(''.join(postorder(root)))
    print(''.join(inorder(root)))
    if i<n-1:
        print()





