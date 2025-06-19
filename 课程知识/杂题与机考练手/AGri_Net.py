import heapq
while True:
    try:
        n=int(input())
    except EOFError:
        break
    matrix=[]
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    visited=[False]*n
    heap=[(0,0)]
    ans=0
    while heap:
        d,u=heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u]=True
        ans+=d
        for v in range(n):
            if not visited[v]:
                heapq.heappush(heap,(matrix[v][u],v))
    print(ans)

