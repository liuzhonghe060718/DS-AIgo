
class DisjointSet:
    def __init__(self,n):
        self.parents=[i for i in range(n)]
    def find(self,x):
        if self.parents[x]!=x:
            self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
    def union(self,x,y):
        root_x=self.find(x)
        root_y=self.find(y)
        if x!=y:
            self.parents[root_y]=root_x
num=int(input())
s=DisjointSet(num)
edges=[]
graph={}
idx=0
for j in range(num-1):
    lst=list(input().split())
    if lst[0] not in graph:
        graph[lst[0]]=idx
        idx+=1
    for i in range(2,len(lst),2):
        edges.append((int(lst[i+1]),lst[0],lst[i]))
        if lst[i] not in graph:
            graph[lst[i]]=idx
            idx+=1
edges.sort()
ans=0
for d,u,v in edges:
    if s.find(graph[u])!=s.find(graph[v]):
        ans+=d
        s.union(graph[u],graph[v])
print(ans)



