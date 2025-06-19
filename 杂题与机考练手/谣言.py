#16:49-16:59
n,m=map(int,input().split())
price=[0]+list(map(int,input().split()))
graph={i:[] for i in range(1,n+1)}
for i in range(m):
    xi,yi=map(int,input().split())
    graph[xi].append(yi)
    graph[yi].append(xi)
visited=[False]*(n+1)
def dfs(u,cost):
    visited[u]=True
    if price[u]<cost:
        cost=price[u]
    for v in graph[u]:
        if not visited[v]:
            cost=dfs(v,cost)
    return cost
ans=0
for i in range(1,n+1):
    if not visited[i]:
        ans+=dfs(i,float('inf'))
print(ans)

