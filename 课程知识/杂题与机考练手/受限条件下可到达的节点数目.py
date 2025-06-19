
n=int(input())
graph={i:[] for i in range(n)}
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
sticted=set(map(int,input().split()))
visited=[False]*n
def dfs(node):
    visited[node]=True
    for u in graph[node]:
        if not visited[u] and u not in sticted:
            dfs(u)
dfs(0)
print(visited.count(True))