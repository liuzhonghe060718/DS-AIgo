n=int(input())
sr,sc=map(int,input().split())
dire=[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]
visited=[[False]*n for _ in range(n)]
visited[sr][sc]=True
can_reach=False
def is_vavid(x,y):
    return 0<=x<n and 0<=y<n and not visited[x][y]
def get_degree(x,y):
    degree=0
    for dx,dy in dire:
        if is_vavid(x+dx,y+dy):
            degree+=1
    return degree
def dfs(x0,y0,idx):
    global can_reach
    if idx==n*n:
        can_reach=True
        return
    if can_reach:
        return
    choice=[]
    for dx,dy in dire:
        nx,ny=x0+dx,y0+dy
        if is_vavid(nx,ny):
            choice.append((get_degree(nx,ny),nx,ny))
    choice.sort()
    for _,nx,ny in choice:
        visited[nx][ny] = True
        dfs(nx,ny,idx+1)
        if can_reach:
            return
        visited[nx][ny]=False
dfs(sr,sc,1)
print('success' if can_reach else 'fail')



