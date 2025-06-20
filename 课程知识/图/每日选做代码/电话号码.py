t=int(input())
class Treenode:
    def __init__(self):
        self.children=[None for _ in range(10)]
        self.count=0
def insert(root,key):
    cur=root
    for c in key:
        cur.count+=1
        if cur.children[c] is None:
            new_node=Treenode()
            cur.children[c]=new_node
        cur=cur.children[c]

for _ in range(t):
    n=int(input())
    words=[]
    root0=Treenode()
    ac='YES'
    for i in range(n):
        words.append(list(map(int,list(input()))))
    words.sort(key=lambda x:len(x),reverse=True)
    for word in words:
        if not insert(root0,word):
            ac='NO'
            break
    print(ac)
