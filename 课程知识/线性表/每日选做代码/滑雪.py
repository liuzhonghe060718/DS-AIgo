import heapq
r,c=map(int,input().split())
matrix=[]
for _ in range(r):
    matrix.append(list(map(int,input().split())))
dp=[[1 for _ in range(c)]for _ in range(r)]
heap = [(matrix[i][j], i, j) for i in range(r) for j in range(c)]
heapq.heapify(heap)
dire=[(0,1),(0,-1),(1,0),(-1,0)]
while heap:
    height,x0,y0=heapq.heappop(heap)
    for dx,dy in dire:
        nx,ny=x0+dx,y0+dy
        if 0<=nx<r and 0<=ny<c and height>matrix[nx][ny]:
            dp[x0][y0]=max(dp[x0][y0],dp[nx][ny]+1)
ans=1
for i in range(r):
    ans=max(ans,max(dp[i]))
print(ans)
