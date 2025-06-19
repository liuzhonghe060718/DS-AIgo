from collections import deque
n,p=map(int,input().split())
values={}
graph={i:{} for i in range(1,n+1)}
indegree=[0]*(n+1)
out=[0]*(n+1)
for i in range(1,n+1):
    values[i]=tuple(map(int,input().split()))
for _ in range(p):
    i,j,w=map(int,input().split())
    if j in graph[i]:
        graph[i][j]+=w
    else:
        graph[i][j]=w
        indegree[j]+=1
        out[i]+=1
queue=deque()
stack=[]
in_level=set()
for i in range(1,n+1):
    if indegree[i]==0:
        queue.append(i)
        in_level.add(i)
while queue:
    u=queue.popleft()
    stack.append(u)
    for v in graph[u]:
        indegree[v]-=1
        if indegree[v]==0:
            queue.append(v)
if len(stack)<len(graph):
    print('NULL')
    exit()
ans=[0]*(n+1)
for u in stack:
    if u in in_level:
        ans[u]=values[u][0]
    else:
        ans[u]-=values[u][1]
    if ans[u]>0:
        for v in graph[u]:
            ans[v]+=graph[u][v]*ans[u]
idx=0
result=[]
for i in range(1,n+1):
    if out[i]==0 and ans[i]>0:
        result.append((i,str(i)+' '+str(ans[i])))
        idx+=1
result.sort()
for x in result:
    print(x[1])
if idx==0:
    print('NULL')