#16:30-16:47
class DisjointSet:
    def __init__(self,m):
        self.parent=[i for i in range(m)]
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        if root_y!=root_x:
            self.parent[root_y]=root_x
n=int(input())
equal=[]
unequal=[]
build={}
idx=0
for j in range(n):
    s=input()
    if s[0] not in build:
        build[s[0]]=idx
        idx+=1
    if s[-1] not in build:
        build[s[-1]]=idx
        idx+=1
    if s[1]=='!':
        unequal.append((s[0],s[-1]))
    else:
        equal.append((s[0],s[-1]))
s=DisjointSet(len(build))
for a,b in equal:
    s.union(build[a],build[b])
for c,d in unequal:
    if s.find(build[c])==s.find(build[d]):
        print('False')
        exit()
print('True')
