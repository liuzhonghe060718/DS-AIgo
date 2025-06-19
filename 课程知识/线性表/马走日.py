dire=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
t=int(input())
for _ in range(t):
    n,m,x0,y0=map(int,input().split())
    visited=[[False for _ in range(m)]for _ in range(n)]
    ans=0
    def backtrack(num,x,y):
        global ans
        if num==n*m:
            ans+=1
            return
        for dx,dy in dire:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny]=True
                backtrack(num+1,nx,ny)
                visited[nx][ny]=False
    visited[x0][y0]=True
    backtrack(1,x0,y0)
    print(ans)
