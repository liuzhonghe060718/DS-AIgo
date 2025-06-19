class DisjointSet:
    def __init__(self,num):
        self.parent=list(range(num))
    def find(self,x0):
        if self.parent[x0]!=x0:
            self.parent[x0]=self.find(self.parent[x0])
        return self.parent[x0]
    def union(self,x0,y0):
        self.parent[y0]=x0






while True:
    try:
        n,m=map(int,input().split())
    except EOFError:
        break
    water=DisjointSet(n)
    for i in range(m):
        x,y=map(int,input().split())
        x-=1
        y-=1
        root_x=water.find(x)
        root_y=water.find(y)
        if root_x==root_y:
            print('Yes')
        else:
            water.union(root_x,root_y)
            print('No')
    ans=set()
    for i in range(n):
        ans.add(water.find(i)+1)
    print(len(ans))
    print(' '.join(map(str,sorted(list(ans)))))


