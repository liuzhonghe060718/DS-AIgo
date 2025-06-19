n=int(input())
m=int(input())
dire=[(1,0),(0,1),(-1,0),(0,-1)]
matrix=[['' for _ in range(m)]for _ in range(n)]
for y in range(n):
    s=list(map(int,input().split()))
    for x in range(m):
        word=bin(s[x])[2:]
        matrix[y][x]='0'*(4-len(word))+word
visited=[[False for _ in range(m)]for _ in range(n)]
def dfs(x0,y0):
    ans=1
    visited[x0][y0]=True
    for dx in range(4):
        nx,ny=x0+dire[dx][0],y0+dire[dx][1]
        if 0<=nx<n and 0<=ny<m and matrix[x0][y0][dx]=='0' and not visited[nx][ny]:
            ans+=dfs(nx,ny)
    return ans
result=0
max_b=1
for x in range(n):
    for y in range(m):
        if not visited[x][y]:
            result+=1
            max_b=max(dfs(x,y),max_b)
print(result)
print(max_b)
