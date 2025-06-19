
class DisjointSet:
    def __init__(self,num):
        self.parent=list(range(num))
    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        root_x,root_y=self.find(x),self.find(y)
        if root_x!=root_y:
            self.parent[root_y]=root_x
number=1
while True:
    n,m=map(int,input().split())
    people={i for i in range(1,n+1)}
    if m==n==0:
        break
    religions=DisjointSet(n)
    religion=set()
    for _ in range(m):
        i,j=map(int,input().split())
        religions.union(i-1,j-1)
    ans=0
    for p in range(n):
        a=religions.find(p)
        if a not in religion:
            religion.add(a)
            ans+=1
    print(f'Case {number}: {ans}')
    number+=1




