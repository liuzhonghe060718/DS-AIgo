from collections import deque
class Treenode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build_tree(s):
    stack=[]
    for word in s:
        if word.islower():
            stack.append(Treenode(word))
        else:
            symbol=Treenode(word)
            symbol.right=stack.pop()
            symbol.left=stack.pop()
            stack.append(symbol)
    return stack.pop()

def level_order(root):
    queue=deque([root])
    ans=[]
    while queue:
        now_node=queue.popleft()
        if now_node.left:
            queue.append(now_node.left)
        if now_node.right:
            queue.append(now_node.right)
        ans.append(now_node.val)
    ans.reverse()
    return ''.join(ans)
n=int(input())
for _ in range(n):
    words=input()
    node=build_tree(words)
    print(level_order(node))

