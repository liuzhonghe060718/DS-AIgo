from collections import defaultdict
n,m=map(int,input().split())
graph=defaultdict(list)
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
visited=[False]*n
def dfs(x,l):
    visited[x]=True
    for y in graph[x]:
        if not visited[y]:
            if dfs(y,x):
                return True
        elif y!=l:
            return True
    return False
idx=0
has_cycle=False
for i in range(n):
    if not visited[i]:
        if dfs(i,None):
            has_cycle=True
        idx+=1
print('connected:yes' if idx==1 else 'connected:no')
print('loop:yes'if has_cycle else 'loop:no')


