class Treenode:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
n=int(input())
def parse_tree(s):
    node=None
    stack=[]
    for char in range(len(s)):
        if s[char].isalpha():
            node=Treenode(s[char])
            if stack:
                if stack[-1].left is None :
                    if s[char-2]!='*':
                        stack[-1].left=node
                    else:
                        stack[-1].right=node
                else:
                    stack[-1].right=node
        elif s[char]=='(':
                stack.append(node)
        elif s[char]==')':
            if stack:
                node=stack.pop()
    return node
def preorder(nodes):
    ans=[nodes.val]
    if nodes.left is not None:
        ans.extend(preorder(nodes.left))
    if nodes.right is not None:
        ans.extend(preorder(nodes.right))
    return ans
def midorder(nodes):
    ans = []
    if nodes.left is not None:
        ans.extend(midorder(nodes.left))
    ans.append(nodes.val)
    if nodes.right is not None:
        ans.extend(midorder(nodes.right))
    return ans
for _ in range(n):
    word=input()
    root=parse_tree(word)
    print(''.join(preorder(root)))
    print(''.join(midorder(root)))




