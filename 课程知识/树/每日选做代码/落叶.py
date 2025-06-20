active=True
class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def insert(word,node):
    if node is None:
        return Treenode(word)
    if node.val>word:
        node.left=insert(word,node.left)
    else:
        node.right=insert(word,node.right)
    return node
def preorder(node):
    if node is None:
        return ''
    ans=node.val
    ans+=preorder(node.left)
    ans+=preorder(node.right)
    return ans
while active:
    tree=[]
    while True:
        a=input()
        if a=='*':
            break
        if a=='$':
            active=False
            break
        tree.append(a)
    root=Treenode(tree[-1])
    for words in tree[::-1][1:]:
        for x in words:
            insert(x,root)
    print(preorder(root))



