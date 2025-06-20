from collections import deque
t=int(input())
dire=[(0,1),(0,-1),(1,0),(-1,0)]
for _ in range(t):
    r,c=map(int,input().split())
    matrix=[]
    for i in range(r):
        s=input()
        if 'S' in s:
            start=(i,s.index('S'))
        if 'E' in s:
            end=(i,s.index('E'))
        matrix.append(s)
    visited=[[False]*c for i in range(r)]
    visited[start[0]][start[1]]=True
    queue=deque([[start[0],start[1],0]])
    def bfs():
        while queue:
            x0,y0,time=queue.popleft()
            for dx,dy in dire:
                nx,ny=x0+dx,y0+dy
                if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and matrix[nx][ny]!='#':
                    if matrix[nx][ny]=='E':
                        return time+1
                    queue.append([nx,ny,time+1])
                    visited[nx][ny]=True
        return 'oop!'
    print(bfs())

