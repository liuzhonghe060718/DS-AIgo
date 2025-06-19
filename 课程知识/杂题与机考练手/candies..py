import heapq
n,m=map(int,input().split())
graph={i:[] for i in range(1,n+1)}
for i in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
def dijkstra(start,end):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d>distance[u]:
            continue
        for v, w in graph[u]:
            if w + d < distance[v]:
                distance[v] = d + w
                heapq.heappush(heap, (d + w, v))
    return distance[end]
print(dijkstra(1,n))