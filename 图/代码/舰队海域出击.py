from collections import defaultdict
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    graph=defaultdict(list)
    for i in range(m):
        x,y=map(int,input().split())
        graph[x].append(y)
    active=True
    visited=[0]*(n+1)#0未访问，1路径中，2结束
    def dfs(u):
        global active
        visited[u]=1
        for v in graph[u]:
            if visited[v]==0:
                dfs(v)
                if not active:
                    return
            elif visited[v]==1:
                active=False
                return
        visited[u]=2
    ans='No'
    for i in range(1,n+1):
        if not visited[i] and active:
            dfs(i)
    print(ans if active else 'Yes')