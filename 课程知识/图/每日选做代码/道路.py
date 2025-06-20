import heapq
k=int(input())
n=int(input())
r=int(input())
graph=[[] for i in range(n+1)]
for _ in range(r):
    s,d,L,T=map(int,input().split())
    graph[s].append((d,L,T))
dp=[{} for i in range(n+1)]
dp[1][0]=0
heap=[(0,1,0)]
heapq.heapify(heap)
while heap:
    meter,u,cost=heapq.heappop(heap)
    if u==n:
        print(meter)
        exit()
    if cost in dp[u] and dp[u][cost]<meter:
        continue
    for v,l,t in graph[u]:
        if cost+t<=k and (cost+t not in dp[v] or dp[v][cost+t]>meter+l):
            dp[v][cost+t]=meter+l
            heapq.heappush(heap,(meter+l,v,cost+t))
print(-1)
