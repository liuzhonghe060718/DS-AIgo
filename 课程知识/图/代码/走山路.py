import heapq

m,n,p=map(int,input().split())
dire=[(0,1),(0,-1),(-1,0),(1,0)]
matrix=[]
for _ in range(m):
    matrix.append(list(input().split()))
def dijkstra(sx,sy,ex,ey):
    if (sx, sy) == (ex, ey):
        return 0
    distance=[[float('inf')]*n for _ in range(m)]
    visited=[[False]*n for _ in range(m)]
    distance[sx][sy] = 0
    heap=[(0,sx,sy)]
    heapq.heapify(heap)
    while heap:
        d,x0,y0=heapq.heappop(heap)
        if visited[x0][y0]:
            continue
        visited[x0][y0]=True
        for dx,dy in dire:
            nx,ny=x0+dx,y0+dy
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                height=abs(int(matrix[x0][y0])-int(matrix[nx][ny]))
                if not visited[nx][ny] and distance[nx][ny]>d+height:
                    distance[nx][ny]=d+height
                    heapq.heappush(heap,(distance[nx][ny],nx,ny))
    return distance[ex][ey] if distance[ex][ey] !=float('inf') else 'NO'


for _ in range(p):
    sx0,sy0,ex0,ey0=map(int,input().split())
    if matrix[sx0][sy0]=='#' or matrix[ex0][ey0]=='#':
        print('NO')
        continue
    print(dijkstra(sx0,sy0,ex0,ey0))
