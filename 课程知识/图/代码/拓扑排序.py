from collections import defaultdict, deque

v,a=map(int,input().split())
graph={i:[] for i in range(1,v+1)}
indegree=defaultdict(int)
for _ in range(a):
    x,y=map(int,input().split())
    graph[x].append(y)
    indegree[y]+=1
queue=deque([])
active=True
ans=[]
visited=[0]+[False]*v
for u in graph:
    graph[u].sort()
    if active  and indegree[u]==0:
        queue.append(u)
        active=False
        visited[u]=True
while queue:
    u=queue.popleft()
    ans.append('v'+str(u))
    for q in graph[u]:
        indegree[q]-=1
    for q in range(1,v+1):
        if not visited[q] and indegree[q]==0:
            queue.append(q)
            visited[q]=True
            break
print(' '.join(ans))


