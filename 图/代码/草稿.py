from 最小奖金方案 import graph
from collections import deque
n=int(input())
visited=[0]*n
has_cycle=False
def dfs(u):
    global has_cycle
    if visited[u]==1:
        has_cycle=True
        return
    if visited[u]==2:
        return
    visited[u]=1
    for v in graph[u]:
        dfs(v)
        if has_cycle:
            return
    visited[u]=2
queue=deque()
indegree=[0]*n
ans=[]
for u in graph:
    for v in graph[u]:
        indegree[v]+=1
for x in range(n):
    if indegree[x]==0:
        queue.append(x)
while queue:
    u=queue.popleft()
    ans.append(u)
    for v in graph[u]:
        indegree[v]-=1
        if indegree[v]==0:
            queue.append(v)
if

