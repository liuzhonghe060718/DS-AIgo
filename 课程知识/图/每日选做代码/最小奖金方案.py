n,m=map(int,input().split())
graph={i:[] for i in range(n)}
for _ in range(m):
    a,b=map(int,input().split())
    graph[b].append(a)
stack=[]
visited=[False]*n
def dfs(u):
    if visited[u]:
        return
    for v in graph[u]:
        dfs(v)
    visited[u]=True
    stack.append(u)
for u in range(n):
    if not visited[u]:
        dfs(u)
stack.reverse()
money={i:0 for i in range(n)}
for i in stack:
    for j in graph[i]:
        money[j]=max(money[j],money[i]+1)
print(100*n+sum(money.values()))