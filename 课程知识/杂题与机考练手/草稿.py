t=int(input())
dire=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]
for _ in range(t):
    n,m,x,y=map(int,input().split())
    visited=[[False]*m for _ in range(n)]
    ans=0
    def dfs(x0,y0,idx):
        global ans
        if idx==m*n:
            ans+=1
        for dx,dy in dire:
            nx,ny=x0+dx,y0+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny,idx+1)
                visited[nx][ny]=False
    visited[x][y]=True
    dfs(x,y,1)
    print(ans)
