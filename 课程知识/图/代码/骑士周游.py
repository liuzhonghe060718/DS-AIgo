n=int(input())
sr,sc=map(int,input().split())
dire=[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]

def is_valid_move(x,y,board,n):
    if 0 <= x < n and 0 <= y < n and not board[x][y]:
        return True
    return False

def get_degree(x,y,board):
    count=0
    for dx,dy in dire:
        nx,ny=x+dx,y+dy
        if is_valid_move(nx,ny,board,n):
            count+=1
    return count


visited=[[False]*n for _ in range(n)]
def dfs(x0,y0,idx):
    if idx==n*n:
        return True
    next_moves=[]
    for dx,dy in dire:
        nx,ny=x0+dx,y0+dy
        if is_valid_move(nx,ny,visited,n):
            degree=get_degree(nx,ny,visited)
            next_moves.append((degree,nx,ny))
    next_moves.sort()
    for _,nx,ny in next_moves:
        visited[nx][ny]=True
        if dfs(nx,ny,idx+1):
            return True
        visited[nx][ny]=False
    return False
visited[sr][sc]=True
print('success'if dfs(sr,sc,1) else 'fail')
